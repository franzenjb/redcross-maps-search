#!/usr/bin/env python3
"""
Extract ALL resources from the Red Cross Maps portal for complete indexing
"""

from bs4 import BeautifulSoup
import json
import re

print("📊 Extracting complete Red Cross Maps inventory...")

with open('redcross_maps_page.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Extract ALL links with better categorization
all_resources = []

# Find all links
links = soup.find_all('a', href=True)

# State patterns
state_patterns = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
    'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
    'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho',
    'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas',
    'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
    'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada',
    'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',
    'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
    'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
    'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia',
    'WI': 'Wisconsin', 'WY': 'Wyoming', 'DC': 'District of Columbia',
    'PR': 'Puerto Rico', 'VI': 'Virgin Islands', 'GU': 'Guam', 'AS': 'American Samoa'
}

for link in links:
    href = link.get('href', '').strip()
    text = link.get_text(strip=True)

    if not href or href == '#':
        continue

    # Build full URL
    if href.startswith('/'):
        full_url = f"https://maps.redcross.org{href}"
    elif not href.startswith('http'):
        full_url = f"https://maps.redcross.org/website/maps/{href}"
    else:
        full_url = href

    # Determine category based on text and URL patterns
    category = 'Other'
    resource_type = 'Link'
    state_codes = []

    # Check for state codes in URL - check both abbreviation and full name
    for code, name in state_patterns.items():
        # Check for state abbreviation (e.g., /FL/, RCFL, _FL_)
        if f'/{code}/' in href.upper() or f'RC{code}' in href.upper() or f'_{code}_' in href.upper():
            state_codes.append(code)
            break
        # Check for full state name in path (e.g., /Florida/)
        if f'/{name}/' in href or f'/{name.replace(" ", "")}/' in href:
            state_codes.append(code)
            break

    # Categorize based on content
    text_lower = text.lower()
    href_lower = href.lower()

    if 'chapter' in text_lower:
        category = 'Organization'
        resource_type = 'Chapter Map'
    elif 'region' in text_lower:
        category = 'Organization'
        resource_type = 'Regional Map'
    elif 'evacuation' in text_lower or 'storm surge' in text_lower:
        category = 'Emergency Response'
        resource_type = 'Evacuation/Storm Surge'
    elif 'population' in text_lower or 'census' in text_lower or 'density' in text_lower:
        category = 'Demographics'
        resource_type = 'Population Data'
    elif 'congressional' in text_lower or 'district' in text_lower:
        category = 'Political Boundaries'
        resource_type = 'Congressional Districts'
    elif 'federal lands' in text_lower or 'reservation' in text_lower:
        category = 'Land Management'
        resource_type = 'Federal Lands'
    elif 'hydrology' in text_lower or 'water' in text_lower:
        category = 'Geography'
        resource_type = 'Hydrology'
    elif 'precipitation' in text_lower or 'rainfall' in text_lower:
        category = 'Weather'
        resource_type = 'Precipitation'
    elif 'physical' in text_lower or 'topograph' in text_lower:
        category = 'Geography'
        resource_type = 'Physical Features'
    elif 'weather' in href_lower or 'tropical' in href_lower:
        category = 'Weather'
        resource_type = 'Weather/Tropical'
    elif 'fema' in href_lower:
        category = 'Federal Resources'
        resource_type = 'FEMA'
    elif 'noaa' in href_lower or 'nws' in text_lower:
        category = 'Federal Resources'
        resource_type = 'NOAA/NWS'
    elif 'usgs' in href_lower:
        category = 'Federal Resources'
        resource_type = 'USGS'
    elif 'arcgis' in href_lower:
        category = 'GIS Tools'
        resource_type = 'ArcGIS Portal'
    elif '.pdf' in href_lower:
        category = 'Maps'
        resource_type = 'PDF Map'

    resource = {
        'title': text or 'Untitled',
        'url': full_url,
        'category': category,
        'type': resource_type,
        'states': state_codes if state_codes else ['National'],
        'original_text': text,
        'filename': href.split('/')[-1] if '/' in href else href
    }

    all_resources.append(resource)

# Remove duplicates based on URL
unique_resources = []
seen_urls = set()

for resource in all_resources:
    if resource['url'] not in seen_urls:
        seen_urls.add(resource['url'])
        unique_resources.append(resource)

# Sort by category and title
unique_resources.sort(key=lambda x: (x['category'], x['title']))

# Save complete inventory
with open('redcross_complete_inventory.json', 'w') as f:
    json.dump(unique_resources, f, indent=2)

# Generate JavaScript array for the search engine
js_array = 'const completeResourceDatabase = [\n'
for resource in unique_resources:
    states_str = json.dumps(resource['states'])
    js_array += f'''    {{
        title: "{resource['title'].replace('"', '\\"')}",
        url: "{resource['url']}",
        category: "{resource['category']}",
        type: "{resource['type']}",
        states: {states_str}
    }},\n'''
js_array += '];\n'

with open('redcross_resources.js', 'w') as f:
    f.write(js_array)

# Print summary
print(f"\n✅ Extracted {len(unique_resources)} unique resources")

# Category breakdown
categories = {}
for resource in unique_resources:
    cat = resource['category']
    categories[cat] = categories.get(cat, 0) + 1

print("\n📊 Resources by Category:")
for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
    print(f"  {cat}: {count}")

# Type breakdown
types = {}
for resource in unique_resources:
    typ = resource['type']
    types[typ] = types.get(typ, 0) + 1

print("\n📊 Resources by Type:")
for typ, count in sorted(types.items(), key=lambda x: x[1], reverse=True)[:15]:
    print(f"  {typ}: {count}")

print(f"\n✅ Saved to redcross_complete_inventory.json and redcross_resources.js")