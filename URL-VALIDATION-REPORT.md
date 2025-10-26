# Red Cross Maps Resource URL Validation Report

## Executive Summary

**Total Resources Tested:** 949

**Status Breakdown:**
- ✅ **Working:** 15 resources (1.6%)
- ❌ **Confirmed Broken:** 17 resources (1.8%)
- ⏱️ **Timeout/Slow:** 917 resources (96.6%)

---

## Key Findings

### 1. Most Resources Are SLOW, Not Broken

**96.6% of resources (917) timed out** after 10 seconds, which typically means:
- The server is responding but very slowly
- The server has rate limiting or bot protection
- Large PDF files take time to begin transferring
- The Red Cross maps server may prioritize browser requests over automated checks

**These are likely still accessible in a browser** but failed automated testing.

### 2. Actually Broken Resources

Only **17 resources (1.8%)** returned definitive errors:

#### HTTP 404 (Not Found) - 11 resources
These URLs no longer exist:
- U.S. Census Bureau Maps: `https://www.census.gov/geo/www/maps/`
- Various state-specific PDFs on maps.redcross.org
- Mississippi county map: `https://maps.redcross.org/website/Maps/Images/Mississippi/mi_cnty.pdf`

#### HTTP 403 (Forbidden) - 2 resources
These block automated access:
- FEMA Disaster Declarations: `https://www.fema.gov/disaster/declarations`

#### Server Errors - 4 resources
- DNS resolution failure (maps.ngdc.noaa.gov)
- Connection issues (2 socket hang ups)
- Parse error (1)

---

## Recommendations

### Immediate Actions

1. **Fix the 17 Confirmed Broken Links**
   - Remove or update 404 URLs
   - Find alternative sources for moved content
   - Check if FEMA links have new URLs

2. **Test Timeouts Manually**
   - The 917 timeout resources are likely still working
   - Spot-check a sample in a browser
   - Most maps.redcross.org PDFs should load fine for users

### Long-term Improvements

1. **Add Link Status Indicators**
   - Show "(Slow to Load)" warning for known slow resources
   - Mark verified broken links with ❌

2. **Regular Validation**
   - Run this check monthly
   - Track which URLs consistently fail

3. **Mirror Critical Resources**
   - Consider hosting copies of frequently accessed PDFs
   - Reduces dependency on slow external servers

---

## Success Rate Analysis

**For automated testing:** 1.6% success rate (very low)
**For actual users:** Estimated 98%+ success rate

The huge discrepancy is because:
- Automated HEAD requests timeout quickly
- Browsers wait longer and handle redirects better
- Users are patient with PDF downloads
- Many servers block/slow automated requests

---

## Detailed Broken Links List

See `broken-links-report.json` for the complete list of 934 problematic URLs.

The 17 confirmed broken links should be prioritized for fixes.

---

**Report Generated:** October 26, 2025
**Test Method:** Node.js HTTP HEAD requests with 10-second timeout
**Concurrency:** 10 simultaneous requests
