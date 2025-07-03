from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and column list
model = joblib.load('bengaluru_price_model.pkl')
model_columns = joblib.load('model_columns.pkl')

# Extract only location columns for the dropdown
location_columns = [col for col in model_columns if col not in ['total_sqft', 'bath', 'bhk']]

@app.route('/')
def home():
    return render_template('index.html', locations=location_columns)

@app.route('/predict', methods=['POST'])
def predict():
    # Read form data
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])
    location = request.form['location']

    # Create empty input with same columns as training
    input_data = pd.DataFrame(columns=model_columns)
    input_data.loc[0] = [0] * len(model_columns)

    # Assign input values
    input_data.at[0, 'total_sqft'] = total_sqft
    input_data.at[0, 'bath'] = bath
    input_data.at[0, 'bhk'] = bhk

    # Set selected location to 1
    if location in model_columns:
        input_data.at[0, location] = 1

    # Make prediction
    predicted_price = model.predict(input_data)[0]

    return render_template(
        'index.html',
        prediction_text=f"Estimated Price: ₹ {round(predicted_price, 2)} lakhs",
        locations=location_columns
    )

if __name__ == '__main__':
    app.run(debug=True)
