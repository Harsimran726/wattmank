# WattMank - Solar Energy Analysis Platform
## Technical Documentation

### Table of Contents
1. [Project Setup Instructions](#project-setup-instructions)
2. [Implementation Documentation](#implementation-documentation)
3. [Example Use Cases](#example-use-cases)
4. [Future Improvement Suggestions](#future-improvement-suggestions)

---

## Project Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Google Cloud account with Gemini API access
- Git for version control
- Virtual environment tool (venv or conda)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/wattmonk.git
   cd wattmonk
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Using venv
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Or using conda
   conda create -n wattmonk python=3.8
   conda activate wattmonk
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory:
   ```
   GEMINI_API_KEY=your_google_gemini_api_key_here
   ```

5. **Start the Application**
   ```bash
   uvicorn main:app --reload
   ```

### Directory Structure
```
wattmonk/
├── main.py              # FastAPI application
├── solarsystem.py       # AI analysis logic
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
├── static/             # Static files
└── templates/          # HTML templates
    └── index.html      # Main interface
```

---

## Implementation Documentation

### Core Components

#### 1. Backend (FastAPI)
- **main.py**: Handles HTTP requests and serves the web interface
  - Endpoints:
    - `GET /`: Serves the main interface
    - `POST /analyze`: Processes image uploads and returns analysis

#### 2. AI Analysis (solarsystem.py)
- **Image Processing**:
  - Converts images to base64 for API transmission
  - Handles image format validation
  - Manages temporary file storage

- **Gemini AI Integration**:
  - Uses Google's Gemini model for image analysis
  - Processes rooftop images for solar potential
  - Generates annotated images with solar panel placements

#### 3. Frontend (HTML/JavaScript)
- **User Interface**:
  - Drag-and-drop image upload
  - Real-time analysis display
  - Interactive results visualization

### Key Features Implementation

1. **Image Analysis Pipeline**
   ```python
   def generate(image_path: str, additional_text: str = None) -> dict:
       # Image processing
       # AI analysis
       # Result generation
   ```

2. **Response Format**
   ```json
   {
       "location": "string",
       "mounting": "string",
       "solar_type": "string",
       "roof_area_m2": number,
       "usable_roof_area_m2": number,
       "estimated_panels": number,
       "system_capacity_kw": number,
       "daily_output_kwh": number,
       "monthly_output_kwh": number,
       "estimated_cost_inr": number,
       "monthly_savings_inr": number,
       "payback_period_years": number,
       "recommendation": "string",
       "total_obstacles": "string",
       "breadth": "string",
       "length": "string"
   }
   ```

---

## Example Use Cases

### 1. Residential Rooftop Analysis
**Scenario**: Homeowner wants to assess solar potential
1. Upload rooftop image
2. System analyzes:
   - Available space
   - Obstructions
   - Optimal panel placement
3. Receive detailed report with:
   - Energy generation estimates
   - Cost projections
   - ROI calculations

### 2. Commercial Building Assessment
**Scenario**: Business owner evaluating solar installation
1. Upload commercial building rooftop image
2. System provides:
   - Large-scale installation recommendations
   - Multiple mounting options
   - Detailed financial analysis

### 3. Solar Installation Planning
**Scenario**: Solar company planning installation
1. Upload client's rooftop image
2. System generates:
   - Technical specifications
   - Installation requirements
   - Material estimates

---

## Future Improvement Suggestions

### 1. Enhanced AI Models
- **GPT-4 Vision Integration**
  - Implement GPT-4 Vision for more accurate image analysis
  - Better understanding of complex rooftop structures
  - Improved obstacle detection and classification
  - More detailed environmental impact analysis

- **YOLOv11 Fine-tuning**
  - Train YOLOv11 specifically for solar panel placement
  - Custom dataset creation for rooftop analysis
  - Improved accuracy in:
    - Obstacle detection
    - Shadow analysis
    - Optimal panel placement
    - Structural integrity assessment

### 2. Additional Features
- **3D Modeling**
  - Generate 3D models of rooftops
  - Virtual solar panel placement
  - Shadow simulation throughout the day

- **Weather Integration**
  - Real-time weather data integration
  - Seasonal performance predictions
  - Climate impact analysis

- **Financial Analysis**
  - Integration with local utility rates
  - Government incentive calculations
  - ROI optimization

### 3. User Experience
- **Mobile Application**
  - Native mobile apps for iOS and Android
  - Real-time analysis on mobile devices
  - AR features for on-site assessment

- **Dashboard**
  - User accounts and history
  - Comparison tools
  - Progress tracking

### 4. Technical Improvements
- **Performance Optimization**
  - Caching mechanisms
  - Batch processing
  - Distributed computing

- **Security Enhancements**
  - End-to-end encryption
  - Secure file storage
  - Access control

- **API Expansion**
  - RESTful API for third-party integration
  - Webhook support
  - Developer documentation

### 5. Environmental Impact
- **Carbon Footprint Calculator**
  - CO2 reduction estimates
  - Environmental impact assessment
  - Sustainability reporting

- **Community Features**
  - Share successful installations
  - Community solar projects
  - Environmental impact tracking

---

## Conclusion

WattMank provides a robust foundation for solar energy analysis with significant potential for growth and improvement. The integration of advanced AI models like GPT-4 Vision and fine-tuned YOLOv11 will enhance accuracy and provide more detailed analysis. Future developments will focus on user experience, technical capabilities, and environmental impact assessment. 