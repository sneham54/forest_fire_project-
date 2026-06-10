# Forest Fire Prediction and Simulation using Flask (AI + Map View)

from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import folium
from folium.plugins import HeatMap

app = Flask(__name__)

# ------------------ Fire Risk Prediction using ML ------------------
def predict_fire_risk_with_model():
    df = pd.read_csv("sample_fire_data.csv")
    X = df[["temperature", "humidity", "wind_speed"]]
    y = (df["fire_risk"] > 0.5).astype(int)

    model = DecisionTreeClassifier()
    model.fit(X, y)

    y_pred = model.predict(X).astype(float)
    padded = np.pad(y_pred, (0, 900 - len(y_pred)), mode='constant')
    return padded.reshape(30, 30).astype(float)

# ------------------ Fire Spread Simulation ------------------
def simulate_fire_spread(initial_map, steps=3):
    fire_maps = [initial_map.astype(float)]
    for step in range(steps):
        next_map = fire_maps[-1].copy()
        for i in range(1, next_map.shape[0]-1):
            for j in range(1, next_map.shape[1]-1):
                if fire_maps[-1][i, j] > 0.5:
                    next_map[i-1:i+2, j-1:j+2] = 1.0
        fire_maps.append(next_map.astype(float))
    return fire_maps

# ------------------ Generate Folium Map ------------------
def generate_fire_map(data):
    m = folium.Map(location=[29.6, 78.2], zoom_start=8)
    heat_data = [[29.6 + i*0.01, 78.2 + j*0.01, float(data[i][j])]
                 for i in range(data.shape[0]) for j in range(data.shape[1]) if float(data[i][j]) > 0]
    HeatMap(heat_data).add_to(m)
    m.save("templates/map.html")

# ------------------ Routes ------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    prediction = predict_fire_risk_with_model()
    prediction_list = [[float(cell) for cell in row] for row in prediction.tolist()]
    return jsonify(prediction=prediction_list)

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json.get('fire_map')
    fire_map = np.array(data, dtype=float)
    spread = simulate_fire_spread(fire_map, steps=5)
    spread_list = [[[float(cell) for cell in row] for row in step.tolist()] for step in spread]
    return jsonify(simulation=spread_list)

@app.route('/map')
def map_view():
    fire_data = predict_fire_risk_with_model()
    generate_fire_map(fire_data)
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)




