# American Red Cross Maps Resource Center

An enhanced search portal providing streamlined access to the comprehensive collection of American Red Cross maps, organizational resources, and emergency response materials.

## 🌟 Features

### Intelligent Search
- **State Name Recognition**: Search by full state names ("Florida", "Texas") or abbreviations ("FL", "TX")
- **Multi-field Search**: Searches across titles, categories, resource types, and URLs
- **Real-time Filtering**: 300ms debounced search with instant results

### Sidebar Navigation
- **Category Accordions**: Expandable sections for all 11 resource categories
- **Type Filtering**: Quick filters for Chapter Maps, Regional Maps, Evacuation Routes, etc.
- **Visual Feedback**: Active states and rotating arrows for better UX

### Comprehensive Database
- **949 Total Resources** across all 50 states and territories
- **222 Organizational Maps**: Chapter boundaries and regional structures
- **190 PDF Resources**: Downloadable maps and reference materials
- **12 Emergency Response**: Evacuation routes and storm surge maps
- **103 Weather Resources**: Precipitation and tropical weather data

### Professional Design
- Red Cross brand colors (#ED1B2E)
- Responsive layout with sticky sidebar
- Clean, accessible interface
- Mobile-friendly design

## 📊 Resource Categories

| Category | Count | Description |
|----------|-------|-------------|
| 📊 Organization | 222 | Chapter and regional maps |
| 🚨 Emergency Response | 12 | Evacuation and storm surge maps |
| 👥 Demographics | 59 | Population and census data |
| 🗺️ Geography | 105 | Hydrology and physical features |
| ⛈️ Weather | 103 | Precipitation and tropical weather |
| 🏛️ Federal Resources | 17 | FEMA, NOAA, and USGS links |
| 📄 Maps | 190 | Downloadable PDF maps |
| 🏛️ Political Boundaries | 54 | Congressional districts |
| 🌲 Land Management | 52 | Federal lands and reservations |

## 🚀 Usage

Simply open `index.html` in any modern web browser. No build process or dependencies required!

### Search Examples
- Type **"Florida"** to find all Florida-specific resources
- Type **"evacuation"** to find emergency evacuation maps
- Type **"chapter"** to find organizational chapter maps
- Click category pills to filter by resource type
- Use sidebar accordions to browse by category

## 🛠️ Technical Details

### Built With
- Pure HTML, CSS, and JavaScript
- Tailwind CSS for styling
- No external dependencies for core functionality

### Data Source
All resources are extracted from the official [American Red Cross Maps Portal](https://maps.redcross.org/website/maps/ARC_Map_Links.html).

### State Detection
The extraction script (`extract_all_redcross_resources.py`) automatically:
1. Parses all links from the Red Cross Maps portal
2. Detects state associations from URLs (both abbreviations and full names)
3. Categorizes resources by type and category
4. Generates a searchable JavaScript database

## 📝 Project Structure

```
redcross-maps-search/
├── index.html                          # Main application
├── extract_all_redcross_resources.py   # Data extraction script
└── README.md                           # This file
```

## 🌐 Live Demo

Visit the live application: [Red Cross Maps Search Portal](https://franzenjb.github.io/redcross-maps-search/)

## 📜 License

This is an educational project that provides enhanced search capabilities for publicly available American Red Cross resources. All Red Cross maps and resources remain the property of the American Red Cross.

## 🙏 Acknowledgments

This enhanced search portal builds upon the comprehensive resource collection maintained by the American Red Cross Maps team. The original collection has been indexed and made more searchable to help disaster response professionals and volunteers quickly find the resources they need.

---

**Note**: This is an independent project created to enhance accessibility to Red Cross resources. It is not officially affiliated with or endorsed by the American Red Cross.
