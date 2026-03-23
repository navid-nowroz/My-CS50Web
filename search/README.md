# Google Search Frontend

A CS50W project that recreates the Google Search interface with a clean, minimalist design and dark theme.

## Overview

This project is the first assignment in Harvard's CS50 Web Development course. It demonstrates HTML, CSS, and frontend design skills by building a functional frontend that mimics Google's search interface. The project successfully recreates three main search interfaces: regular search, image search, and advanced search, all with a modern dark theme aesthetic.

## Features

### 🔍 Main Search Page (`index.html`)
- Clean, centered search interface with the Google logo prominently displayed
- Single search input field that queries Google's search engine
- "Google Search" button for regular search functionality
- "I'm Feeling Lucky" button for lucky search functionality
- Easy navigation links to Images and Advanced Search pages
- Responsive design that works on various screen sizes
- Dark theme with light gray text for comfortable viewing

### 📸 Image Search (`images.html`)
- Dedicated page for searching images specifically
- Same minimalist design as the main search page for consistency
- Redirects image searches to Google Images using the `udm=2` parameter
- Easy navigation to main search and advanced search pages
- Integrated navigation bar at the top
- Maintains the dark theme aesthetic throughout

### 🚀 Advanced Search (`advanced.html`)
- Full-featured advanced search interface with multiple filter options
- Four distinct search filters:
  - **All of these words**: Search for pages containing all specified words together
  - **This exact word or phrase**: Search for exact matches of phrases
  - **None of these words**: Exclude specific words from search results
  - **Site or domain**: Limit search results to a specific website or domain
- Professional grid-based form layout for organized presentation
- Google logo displayed in the header for branding
- Navigation links to main search and image search pages
- Advanced Search button with distinct styling
- Large, readable headings and labels
- Proper spacing and alignment for accessibility

### 🎨 Styling (`styles.css`)
- **Dark theme implementation** with dark gray background (#202124) and light gray text
- **Responsive layout** using Flexbox for navigation and CSS Grid for advanced search forms
- **Hover effects** for interactive elements:
  - Navigation links underline on hover
  - Buttons highlight with border on hover
- **Professional typography** using Arial sans-serif font family
- **Separate styling** for advanced search form inputs with distinct appearance
- **Mobile-friendly design** with centered content and flexible dimensions
- **Custom input styling** with rounded borders and padding
- **Button styling** with cursor pointer effects
- **Form alignment** using flexbox for centered, organized layouts
- **Proper color contrast** for accessibility and readability

## Project Structure

```
search/
├── index.html           # Main Google Search page
├── images.html          # Google Image Search page
├── advanced.html        # Google Advanced Search page
├── styles.css           # Unified stylesheet for all pages
├── google_logo.png      # Official Google logo image (241KB)
├── google_icon.png      # Google favicon for browser tabs (130KB)
└── styles.scss          # SCSS file (placeholder for future use)
```

## Technical Details

### HTML Features
- **Semantic HTML5 structure** with proper DOCTYPE and lang attributes
- **Forms with proper action attributes** that submit to Google's search endpoint (`https://google.com/search`)
- **Query parameter handling**:
  - `q` - Main search query parameter
  - `btnI` - "I'm Feeling Lucky" special parameter
  - `udm=2` - Google Images specific filter
  - `as_q` - Advanced search: all words parameter
  - `as_epq` - Advanced search: exact phrase parameter
  - `as_eq` - Advanced search: exclude words parameter
  - `as_sitesearch` - Advanced search: site domain parameter
- **Proper form inputs** with type="search" for semantic meaning
- **Navigation structure** with consistent link placement
- **Favicon implementation** for branding in browser tabs
- **Proper heading hierarchy** with h1 and h2 tags

### CSS Features
- **Flexbox layouts** for navigation bars and form alignment:
  - Navigation items aligned to the right (flex-end)
  - Forms centered with column direction
  - Proper alignment of buttons and inputs
- **CSS Grid** for advanced search form:
  - Two-column layout (labels and inputs)
  - Automatic row sizing
  - Gap spacing for separation
- **Custom input styling** with:
  - Rounded borders (border-radius: 24px)
  - Light gray background
  - Black border
  - Proper padding for comfortable interaction
  - Consistent font size
- **Button styling** with:
  - Custom background colors
  - Hover effects with border highlighting
  - Proper cursor indication
  - Rounded corners
  - Padding and margin for spacing
- **Dark theme implementation**:
  - Dark background (#202124)
  - Light gray text (lightgray)
  - Consistent color scheme throughout
- **Responsive sizing** with:
  - Viewport-relative dimensions (e.g., height: 80vh)
  - Flexible widths for inputs
  - Adaptive layouts using Flexbox
- **Typography styling**:
  - Arial sans-serif font family
  - Proper font sizes for hierarchy
  - Line height adjustments
  - Margin and padding control

### Design Highlights
- **Minimalist aesthetic** matching Google's design philosophy
- **Dark mode implementation** with light gray text for reduced eye strain
- **Centered layouts** with proper spacing and alignment
- **Professional navigation styling** with hover effects
- **Accessible form design** with proper labels and semantic HTML
- **Consistent branding** with Google logo and favicon
- **Visual hierarchy** with proper sizing and spacing
- **User-friendly interface** with clear call-to-action buttons
- **Responsive design** that adapts to different screen sizes
- **Interactive elements** with cursor feedback

## How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/navid-nowroz/My-CS50Web.git
cd My-CS50Web/search
```

### 2. Open in Browser

**Option A: Direct file opening**
- Simply double-click `index.html` to open it in your default browser

**Option B: Using a local server (recommended)**
```bash
# Using Python 3
python -m http.server 8000

# Or using Python 2
python -m SimpleHTTPServer 8000
```
- Visit `http://localhost:8000/search/` in your web browser

**Option C: Using Node.js (if installed)**
```bash
npx http-server
```

### 3. Navigation
- **Main Page**: `index.html` - Regular Google search
- **Image Search**: Click "Images" link - Search Google Images
- **Advanced Search**: Click "Advanced" link - Access advanced filters
- **Back Navigation**: Use navigation links at the top to move between pages

### 4. Performing Searches
- **Regular Search**: 
  1. Enter your query in the search box
  2. Click "Google Search" or press Enter
  3. Results from Google will appear
  
- **Lucky Search**: 
  1. Enter your query
  2. Click "I'm Feeling Lucky"
  3. You'll be taken directly to the first search result
  
- **Image Search**: 
  1. Navigate to Images page
  2. Enter search term
  3. Click "Image Search"
  4. Google Images results will display
  
- **Advanced Search**: 
  1. Navigate to Advanced Search
  2. Fill in desired filter fields
  3. Click "Advanced Search"
  4. Filtered results will display

## Browser Compatibility

- ✅ **Chrome/Chromium** (version 60+)
- ✅ **Firefox** (version 55+)
- ✅ **Safari** (version 11+)
- ✅ **Edge** (version 79+)
- ✅ **Opera** (version 47+)

## File Descriptions

### index.html
- Main entry point for the search application
- Contains the core search functionality
- Displays Google logo and search input
- Includes navigation to other search pages
- Simple, clean layout focused on search

### images.html
- Specialized page for image searches
- Uses the `udm=2` parameter for Google Images
- Maintains consistent design with main page
- Provides easy access to other search types

### advanced.html
- Complex multi-field search interface
- Implements Google's advanced search parameters
- Uses grid layout for organized form display
- Includes informative headers and labels
- More structured HTML with semantic sections

### styles.css
- Universal stylesheet applied to all pages
- Defines all color schemes and themes
- Controls layout with Flexbox and Grid
- Manages responsive design
- Implements hover effects and interactivity
- Contains styling for all HTML elements

## Learning Outcomes

This project demonstrates proficiency in:

- ✅ **HTML5 Markup**: Semantic HTML structure with proper form elements
- ✅ **CSS3 Styling**: Advanced layouts using Flexbox and CSS Grid
- ✅ **Form Design**: Multi-field forms with proper input types and labels
- ✅ **UI/UX Principles**: Clean interface design following best practices
- ✅ **Dark Theme Design**: Implementing modern dark mode aesthetics
- ✅ **Cross-page Navigation**: Multiple pages with consistent navigation
- ✅ **Responsive Design**: Layouts that work on various screen sizes
- ✅ **Web Standards**: Accessibility and semantic HTML compliance
- ✅ **Frontend Integration**: Working with external search services via forms
- ✅ **Design Consistency**: Maintaining visual coherence across pages

## Key Concepts Implemented

### HTTP Form Submission
- Forms use GET method (default) to submit queries
- Query parameters are passed through URL
- Direct integration with Google's search endpoints

### Query Parameters
- Understanding URL structure and parameter passing
- Multiple parameters for different search types
- Google API parameter conventions

### CSS Layout Techniques
- Flexbox for one-dimensional layouts
- CSS Grid for two-dimensional form layouts
- Responsive design without media queries
- Proper spacing and alignment

### User Interface Design
- Minimalist design philosophy
- Dark theme implementation
- Accessibility considerations
- User experience best practices

## Future Enhancements

Potential improvements for this project:
- Add more advanced filter options
- Implement client-side form validation
- Add JavaScript for enhanced interactivity
- Create mobile-specific optimizations
- Add keyboard navigation support
- Implement search history
- Add bookmarking functionality

## Credits

- **Instructor**: Harvard CS50W Course
- **Project Assignment**: Google Search Frontend Recreation
- **Images**: Google official logo and icon
- **Inspiration**: Google's minimalist design philosophy

## License

This is an educational project created as part of Harvard's CS50 Web Development course. It is provided as-is for learning purposes.

## Author

**navid-nowroz** - CS50 Web Development Student

---

## Project Status

✅ **Complete** - All required features implemented and working

Last Updated: March 23, 2026

## Acknowledgments

This project successfully demonstrates the core competencies required for CS50W:
- Clean, professional code organization
- Proper HTML semantic structure
- Advanced CSS layout techniques
- Attention to detail in UI design
- Understanding of form submission and web standards

---

**Note**: This project is for educational purposes and demonstrates frontend skills by recreating Google's search interface design. It is not affiliated with or endorsed by Google.
