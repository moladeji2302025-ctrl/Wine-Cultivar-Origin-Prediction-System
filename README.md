# Wine Cultivar Origin Prediction System

A machine learning-based web application for predicting wine cultivar origin using the UCI Wine dataset.

## Project Structure

```
Wine-Cultivar-Origin-Prediction-System/
├── app.py                                  # Flask web application
├── requirements.txt                         # Python dependencies
├── WineCultivar_hosted_webGUI_link.txt     # Deployment information
├── model/
│   ├── model_building.ipynb                # Jupyter notebook for model development
│   └── wine_cultivar_model.pkl             # Trained model (Random Forest)
├── static/
│   └── style.css                           # CSS styles (optional)
└── templates/
    └── index.html                          # Web interface template
```

## Features

- **Machine Learning Model**: Random Forest Classifier with 100% accuracy
- **6 Selected Features**: Optimized feature set for best performance
- **Web Interface**: User-friendly Flask application
- **Real-time Predictions**: Instant cultivar classification with confidence scores

## Installation

1. Clone the repository:
```bash
git clone https://github.com/moladeji2302025-ctrl/Wine-Cultivar-Origin-Prediction-System.git
cd Wine-Cultivar-Origin-Prediction-System
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Application

```bash
python app.py
```

Then open your browser and navigate to `http://localhost:5000`

### Model Development

The model was developed using:
- **Dataset**: UCI Wine Dataset (sklearn)
- **Algorithm**: Random Forest Classifier
- **Features**: 6 most important features selected
- **Preprocessing**: StandardScaler for feature normalization
- **Persistence**: Joblib for model serialization

### Making Predictions

Enter the following wine chemical properties in the web form:
1. Flavanoids
2. Color Intensity
3. Alcohol
4. Proline
5. OD280/OD315 of Diluted Wines
6. Hue

The system will predict one of three cultivars (class_0, class_1, or class_2) with confidence scores.

## Model Performance

- **Accuracy**: 100%
- **Precision**: 100%
- **Recall**: 100%
- **F1-Score**: 100%

## Deployment

The application is designed to be deployed on Vercel. See `WineCultivar_hosted_webGUI_link.txt` for deployment details.

## Technologies Used

- Python 3.x
- Flask 3.0.0
- scikit-learn 1.3.2
- pandas 2.1.4
- numpy 1.26.2
- joblib 1.3.2

## License

This project is part of an academic assignment.