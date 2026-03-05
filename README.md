# 🏠 California House Price Predictor

> *Turning Data Into Decisions — One Prediction at a Time*

A full-stack, end-to-end Machine Learning web application that predicts median house prices across California based on geographic, demographic, and socioeconomic features. Built with FastAPI, Scikit-learn, and a vanilla HTML/CSS/JS frontend.

---

## 📁 Project Structure

```
california-house-price-predictor/
├── backend/
│   ├── main.py                  # FastAPI app with all endpoints
│   ├── user_input.py            # Pydantic input validation model
│   ├── model_improved_2.pkl     # Trained Random Forest model
│   ├── requirements.txt         # Python dependencies
│   └── Dockerfile               # For Hugging Face deployment
│
└── frontend/
    ├── index.html               # Main HTML page
    ├── styles.css               # Styling
    ├── app.js                   # API calls and frontend logic
    └── image3.jpg               # Background image
```

---

## 🧠 Features

- Predicts California house prices using a trained Random Forest Regressor
- Custom feature engineering pipeline built into the model
- Input validation on both frontend (JS) and backend (Pydantic)
- RESTful FastAPI backend with multiple endpoints
- Ocean proximity dropdown with all 5 categories
- Clean, responsive UI with smooth scroll navigation
- Deployed on GitHub Pages + Hugging Face Spaces

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| ML Model | Scikit-learn (Random Forest Regressor) |
| Data Processing | Pandas, NumPy |
| Backend | FastAPI, Uvicorn |
| Frontend | HTML, CSS, JavaScript |
| Frontend Hosting | GitHub Pages |
| Backend Hosting | Hugging Face Spaces (Docker) |

---

## 📊 Input Features

| Feature | Description |
|---|---|
| longitude | Longitude of the block |
| latitude | Latitude of the block |
| housing_median_age | Median age of houses in the block |
| total_rooms | Total rooms across all households |
| total_bedrooms | Total bedrooms across all households |
| population | Total population in the block |
| households | Total number of households |
| median_income | Median income (in tens of thousands) |
| ocean_proximity | Distance category to the ocean |

---

## Engineered Features (inside pipeline)

The model pipeline internally computes:
- bedrooms_per_household — average bedrooms per household
- rooms_per_household_logged — log-transformed rooms per household
- population_per_household_logged — log-transformed population density
- bedrooms_per_household_capped_log — capped and log-transformed bedroom ratio

---

## 🚀 Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/california-house-price-predictor.git
cd california-house-price-predictor
```

### 2. Set up the backend
```bash
cd backend

# Create and activate virtual environment
python -m venv modelenv
modelenv\Scripts\activate       # Windows
source modelenv/bin/activate    # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

### 3. Start the frontend
Open frontend/index.html with Live Server in VS Code
(Right-click the file, then Open with Live Server)

### 4. Open in browser
```
Frontend: http://127.0.0.1:5500
Backend:  http://127.0.0.1:8000
API Docs: http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Welcome message |
| GET | /health | Health check + model version |
| GET | /about | About the API |
| GET | /contact | Contact information |
| POST | /predict | Predict house price |

### Example Request

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "longitude": -122.24,
    "latitude": 37.48,
    "housing_median_age": 7,
    "total_rooms": 883,
    "total_bedrooms": 128,
    "population": 322,
    "households": 126,
    "median_income": 9.3,
    "ocean_proximity": "<1H OCEAN"
  }'
```

### Example Response

```json
{
  "prediction": 414567.48
}
```

---

## 📦 Requirements

```
fastapi
uvicorn
scikit-learn==1.6.1
pandas
numpy
pydantic
```

> Important: The model was trained with scikit-learn==1.6.1. Using a different version will cause a version mismatch error on load.

---

## 🗂️ Model Details

| Detail | Value |
|---|---|
| Algorithm | Random Forest Regressor |
| Dataset | California Housing Dataset (1990 Census) |
| Model Version | 1.0.0 |
| Serialization | Pickle (.pkl) |
| Preprocessing | Custom pipeline with FunctionTransformer + OneHotEncoder |

---

## Known Issues and Notes

- The model is trained on the 1990 California Census dataset, so predicted prices reflect 1990 values, not current market prices.
- The .pkl file must match the scikit-learn version used during training (1.6.1).
- engineer_features must be defined in scope before loading the pickle file.

---

## Developer

Ishita Singh
- Email: singhishita7784@gmail.com
- GitHub: https://github.com/codeishitech

---

## 📄 License

This project is open source and available under the MIT License.

---

Built with love as part of a Machine Learning end-to-end deployment project.
