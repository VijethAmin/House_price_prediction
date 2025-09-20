from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model and the feature column names
model = joblib.load('bengaluru_price_model.pkl')
model_columns = joblib.load('model_columns.pkl')

# Extract location columns (one-hot encoded) for dropdown
location_columns = [col for col in model_columns if col not in ['total_sqft', 'bath', 'bhk']]

@app.route('/')
def home():
    return render_template('index.html', locations=location_columns)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs from the form
        total_sqft = float(request.form['total_sqft'])
        bath = int(request.form['bath'])
        bhk = int(request.form['bhk'])
        selected_location = request.form['location']

        # Initialize input with zero values
        input_data = pd.DataFrame(columns=model_columns)
        input_data.loc[0] = [0] * len(model_columns)

        # Set numeric features
        input_data.at[0, 'total_sqft'] = total_sqft
        input_data.at[0, 'bath'] = bath
        input_data.at[0, 'bhk'] = bhk

        # Match selected location exactly to model column
        matched_location = next((col for col in location_columns if col.lower() == selected_location.lower()), None)
        if matched_location:
            input_data.at[0, matched_location] = 1
        else:
            # Fallback: If somehow location not found, use 'other' if it exists
            if 'other' in model_columns:
                input_data.at[0, 'other'] = 1

        # Predict the price
        predicted_price = model.predict(input_data)[0]

        # Prevent negative predictions
        predicted_price = max(0, predicted_price)

        return render_template(
            'index.html',
            prediction_text=f"🏠 Estimated Price: ₹ {round(predicted_price, 2)} lakhs",
            locations=location_columns
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f"❌ Error: {str(e)}",
            locations=location_columns
        )

if __name__ == '__main__':
    app.run(debug=True)
