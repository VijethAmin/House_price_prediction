# 🏠 Bengaluru House Price Prediction

A machine learning web application that predicts real estate prices in Bengaluru, India, using user inputs such as square footage, number of bathrooms, BHK, and location. The model is trained on a real dataset and deployed with a Flask-based interface.

---

## 🚀 Demo

![App Screenshot](https://via.placeholder.com/600x300?text=Include+your+app+screenshot+here)

> 📌 Add your running app screenshot or deployment link if hosted.

---

## 📁 Dataset

- **Source**: [Kaggle - Bengaluru House Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
- **Rows**: 13,320
- **Key Features**: Location, Size (BHK), Total Sqft, Bath, Price

---

## 🧠 Features

- Predicts house prices in ₹ lakhs
- Real-world dataset cleaning & processing
- Model trained using Random Forest Regressor (R² ~ 0.94)
- Clean and modern UI with dropdown selection for location
- Deployed using Flask

---

## 🔧 Tech Stack

| Area           | Tools Used                                 |
|----------------|---------------------------------------------|
| Programming    | Python 3.x                                  |
| Data Science   | Pandas, NumPy, Scikit-learn, Seaborn        |
| Web Framework  | Flask                                       |
| Frontend       | HTML5, CSS3, Google Fonts (Poppins)         |
| Deployment     | Localhost (can be extended to Render/Heroku)|

---

## 📊 Model Performance

| Metric     | Score              |
|------------|-------------------|
| R² Score   | 0.945 ✅           |
| MAE        | ₹1.61 lakhs ✅     |
| RMSE       | ₹21.7 lakhs ✅     |

---

## 📸 UI Screenshot

> Replace the image URL with your own screenshot

![Screenshot](https://via.placeholder.com/600x350?text=Prediction+UI+Screenshot)

---

## 🛠️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/bengaluru-house-price-predictor.git
cd bengaluru-house-price-predictor

# 2. Create and activate a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py
