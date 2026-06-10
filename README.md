# Forest Fire Prediction and Simulation System

## Overview
This project is a Flask-based web application that predicts forest fire risk using a Decision Tree Machine Learning model and simulates fire spread across a grid. The system also generates a heatmap visualization using Folium to represent fire-prone areas.

## Features
- Forest fire risk prediction using Machine Learning
- Fire spread simulation on a 30x30 grid
- Interactive web interface using Flask
- Heatmap visualization using Folium
- Dataset-based prediction using environmental parameters

## Technologies Used
- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Folium
- HTML

## Project Workflow
1. Load forest fire dataset.
2. Train a Decision Tree Classifier.
3. Predict fire-prone areas based on:
   - Temperature
   - Humidity
   - Wind Speed
4. Generate a fire risk grid.
5. Simulate fire spread over multiple steps.
6. Display results and heatmap through a Flask web application.

## Project Structure

```text
forest_fire_project/
│
├── app.py
├── sample_fire_data.csv
│
├── templates/
│   ├── index.html
│   └── map.html
│
└── requirements.txt
```

## Installation

### Clone Repository

```bash
git clone https://github.com/sneham54/Forest-Fire-Prediction-System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

## API Routes

| Route | Description |
|---------|------------|
| / | Home Page |
| /predict | Predict fire risk |
| /simulate | Simulate fire spread |
| /map | Generate heatmap visualization |

## Machine Learning Model
- Algorithm: Decision Tree Classifier
- Input Features:
  - Temperature
  - Humidity
  - Wind Speed
- Output:
  - Fire Risk Classification

## Future Improvements
- Real-time weather data integration
- Advanced ML models (Random Forest, XGBoost)
- Better fire spread algorithms
- Enhanced user interface
- Cloud deployment

## Author
Sneha M
