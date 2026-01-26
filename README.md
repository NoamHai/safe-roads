# Safe Roads Accident Risk Predictor

A demo web application that predicts accident risk based on driving conditions using a FastAPI backend and static frontend. The system provides real-time risk assessment with explainable AI breakdowns.

## 🚀 Features

- **Interactive Web Interface**: Clean, responsive UI for inputting driving conditions
- **Real-time Risk Prediction**: Instant probability calculation with risk categorization
- **Explainable AI**: Detailed breakdown of factors contributing to risk assessment
- **ML-Ready Architecture**: Supports both rule-based and machine learning models
- **Production-Ready Backend**: Modular FastAPI implementation with proper error handling

## 📋 Requirements

- Python 3.8+
- Modern web browser with JavaScript enabled

## 🛠 Installation

### 1. Clone or Download
```powershell
# Navigate to your project directory
cd path\to\your\project
```

### 2. Set up Python Virtual Environment
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

### 3. Install Dependencies
```powershell
# Install core dependencies
pip install -r requirements.txt

# Optional: Install development dependencies for testing
pip install -r requirements-dev.txt
```

### 4. Configure Environment (Optional)
```powershell
# Copy example environment file
copy .env.example .env

# Edit .env file if needed (default values work for development)
```

## 🚀 Running the Application

### One-Command Start
```powershell
# From project root directory
python -m uvicorn backend.app:app --reload --port 8000
```

### Access the Application
- Open your web browser and navigate to: `http://127.0.0.1:8000`
- The frontend will load automatically
- Select driving conditions and click "Predict risk"

### Alternative: Manual Frontend Serving
If you prefer to serve the frontend separately:
```powershell
# Terminal 1: Start backend
python -m uvicorn backend.app:app --reload --port 8000

# Terminal 2: Serve frontend (from project root)
cd frontend
python -m http.server 5500
```
Then access: `http://127.0.0.1:5500` (with backend CORS configured)

## 🧪 Testing

### Automated Testing
```powershell
# Install development dependencies
pip install -r requirements-dev.txt

# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_predict.py

# Run tests with coverage
pytest --cov=backend --cov-report=html
```

### Manual Testing
1. Start the application as described above
2. Test various combinations of:
   - Road types: Urban, Highway
   - Weather: Clear, Rain, Fog
   - Time of day: Day, Night
   - Lighting: Daylight, Dark with/without streetlights
   - Junction: No junction, Junction
   - Road surface: Dry, Wet, Unknown

### API Testing
```powershell
# Test the prediction endpoint directly
curl -X POST "http://127.0.0.1:8000/predict" ^
  -H "Content-Type: application/json" ^
  -d "{\"road_type\":\"urban\",\"weather\":\"clear\",\"time_of_day\":\"day\",\"lighting\":\"daylight\",\"junction\":\"no_junction\",\"road_surface\":\"dry\"}"
```

### Automated Testing (Development)
```powershell
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests (when implemented)
pytest
```

## 📁 Project Structure

```
safe-roads/
├── backend/                 # FastAPI backend
│   ├── app.py              # Main application and middleware
│   ├── config.py           # Configuration settings
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py      # Pydantic models and enums
│   ├── routes/
│   │   ├── __init__.py
│   │   └── predict.py      # API endpoints
│   └── services/
│       ├── __init__.py
│       └── model_service.py # ML inference logic
├── frontend/               # Static web interface
│   ├── index.html
│   ├── script.js
│   └── style.css
├── tools/                  # Data analysis utilities
│   └── accidents_analysis.py
├── data/                   # Dataset files
│   └── accidents_raw_master.csv
├── docs/                   # Documentation
├── .env.example           # Environment configuration template
├── requirements.txt       # Core dependencies
└── requirements-dev.txt   # Development dependencies
```

## 🔧 Configuration

The application uses the following configuration options (set via `.env` file):

- `APP_NAME`: Application title (default: "Safe Roads API")
- `DEBUG`: Debug mode (default: false)
- `MODEL_PATH`: Path to ML model file (default: "model.pkl")
- `CORS_ORIGINS`: Allowed CORS origins (comma-separated)

## 🤖 ML Model Integration

The system is designed to work with or without a trained ML model:

### Without ML Model
- Uses rule-based risk calculation
- Provides consistent, explainable results
- No external dependencies

### With ML Model
- Place `model.pkl` in the project root
- Model should be trained on the 6 input features
- Must implement `predict_proba()` returning `[p_no_accident, p_accident]`
- System automatically detects and uses ML model
- Falls back to rule-based if model fails

## 🛡️ Error Handling

The application includes comprehensive error handling:

- **Frontend**: Validates API responses, handles network errors, defensive rendering
- **Backend**: Input validation, graceful degradation, detailed logging
- **API**: Structured error responses with appropriate HTTP status codes

## 📚 API Documentation

### POST /predict

Predicts accident risk based on driving conditions.

**Request Body:**
```json
{
  "road_type": "urban|highway",
  "weather": "clear|rain|fog",
  "time_of_day": "day|night",
  "lighting": "daylight|dark_with_streetlights|dark_no_streetlights",
  "junction": "no_junction|junction",
  "road_surface": "dry|wet|unknown"
}
```

**Response:**
```json
{
  "probability": 0.15,
  "risk_percent": 15,
  "breakdown": [
    {
      "factor": "weather",
      "value": "rain",
      "delta": 0.18,
      "note": "Reduced friction + visibility"
    }
  ]
}
```

## 🐛 Troubleshooting

### Backend Won't Start
- Ensure Python virtual environment is activated
- Check that all dependencies are installed: `pip list`
- Verify port 8000 is not in use by another application

### Frontend Not Loading
- Check browser console for JavaScript errors
- Ensure backend is running on port 8000
- Try refreshing the page

### Prediction Errors
- Check browser network tab for API request details
- Verify backend logs for error messages
- Ensure all required fields are provided in the request

## 🔄 CI/CD

This project uses GitHub Actions for continuous integration:

- **Automated Testing**: Runs on every push and pull request
- **Multi-Python Support**: Tests against Python 3.8-3.12
- **Coverage Reports**: Generates test coverage reports
- **Code Quality**: Ensures code works across different environments

### Workflow Status
![CI](https://github.com/your-username/safe-roads/workflows/CI/badge.svg)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is for educational and demonstration purposes.

---

**Built with:** FastAPI, Pydantic, Joblib, HTML/CSS/JavaScript</content>
<parameter name="filePath">c:/Users/Admin/Desktop/5_year/semester_A/final_project/README.md