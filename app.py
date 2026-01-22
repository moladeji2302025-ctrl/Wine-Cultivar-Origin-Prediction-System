from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join('model', 'wine_cultivar_model.pkl')
model_data = joblib.load(model_path)
model = model_data['model']
scaler = model_data['scaler']
selected_features = model_data['selected_features']
target_names = model_data['target_names']

@app.route('/')
def home():
    """Render the home page with input form"""
    return render_template('index.html', features=selected_features)

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    try:
        # Get input values from the form
        input_features = []
        feature_values = {}
        
        for feature in selected_features:
            value = float(request.form.get(feature, 0))
            input_features.append(value)
            feature_values[feature] = value
        
        # Convert to numpy array and reshape
        input_array = np.array(input_features).reshape(1, -1)
        
        # Scale the input
        input_scaled = scaler.transform(input_array)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0]
        
        # Get cultivar name
        cultivar_name = target_names[prediction]
        confidence = probability[prediction] * 100
        
        result = {
            'cultivar_number': int(prediction),
            'cultivar_name': cultivar_name,
            'confidence': round(confidence, 2),
            'all_probabilities': {
                target_names[i]: round(prob * 100, 2) 
                for i, prob in enumerate(probability)
            }
        }
        
        return render_template('index.html', 
                             features=selected_features,
                             prediction=result,
                             input_values=feature_values)
    
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return render_template('index.html', 
                             features=selected_features,
                             error=error_message)

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for predictions"""
    try:
        data = request.get_json()
        
        # Extract features in the correct order
        input_features = [float(data.get(feature, 0)) for feature in selected_features]
        input_array = np.array(input_features).reshape(1, -1)
        
        # Scale and predict
        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0]
        
        result = {
            'cultivar_number': int(prediction),
            'cultivar_name': target_names[prediction],
            'confidence': round(probability[prediction] * 100, 2),
            'all_probabilities': {
                target_names[i]: round(prob * 100, 2) 
                for i, prob in enumerate(probability)
            }
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
