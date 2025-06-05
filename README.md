# WattMank - Solar Energy Analysis Platform

WattMank is an AI-powered platform that analyzes rooftop images to provide detailed solar energy potential assessments. Using Google's Gemini AI model, it offers comprehensive analysis including solar panel placement, energy generation estimates, and financial projections.

## Features

- 📸 Upload rooftop images for analysis
- 🤖 AI-powered solar potential assessment
- 📊 Detailed analysis including:
  - Roof area and usable space calculation
  - Solar panel placement recommendations
  - Energy generation estimates
  - Financial projections and ROI calculations
  - Mounting system recommendations
- 🎯 Visual representation of solar panel placement
- 💰 Cost and savings calculations

## Tech Stack

- **Backend:**
  - FastAPI (Python web framework)
  - Google Gemini AI (for image analysis)
  - LangChain (AI framework)
  - Python-dotenv (environment management)

- **Frontend:**
  - HTML5
  - TailwindCSS (styling)
  - JavaScript (vanilla)
  - Jinja2 (templating)

## Prerequisites

- Python 3.8 or higher
- Google Cloud account with Gemini API access
- Git (for version control)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/harsimran726/wattmonk.git
   cd wattmonk
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory:
   ```
   GEMINI_API_KEY=your_google_gemini_api_key_here
   ```

## Usage

1. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

3. Upload a rooftop image:
   - Click the upload area or drag and drop an image
   - Add any additional context in the text input
   - Click "Send" to start the analysis

4. View the results:
   - The analysis will show both the original image and the AI-generated overlay
   - Detailed metrics and recommendations will be displayed
   - Financial projections and ROI calculations will be shown

## Project Structure

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

## API Endpoints

- `GET /`: Main application interface
- `POST /analyze`: Image analysis endpoint
  - Accepts: Image file and optional text
  - Returns: Analysis results and generated image

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Acknowledgments

- Google Gemini AI for the image analysis capabilities
- FastAPI for the robust backend framework
- TailwindCSS for the beautiful UI components 
