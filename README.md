 🏡 California Housing Price Prediction (Streamlit + ML Models)

This project demonstrates how to build, train, and deploy **linear regression-based models** to predict California housing prices using the **California Housing Dataset** from Scikit-Learn.  
It includes data preprocessing, model training (Linear, Ridge, Lasso, ElasticNet), model saving/loading, and a **Streamlit web app** for real-time predictions.

## 🚀 Project Overview

### 🔹 Steps Covered
1. **Data Loading & Preprocessing**
   - Used the California Housing dataset (`fetch_california_housing`).
   - Cleaned, scaled, and split the data into train/test sets.

2. **Model Training**
   - Trained four regression models:
     - Linear Regression
     - Ridge Regression
     - Lasso Regression
     - Elastic Net Regression
   - Achieved ~**67% accuracy (R² Score)** across models.

3. **Model Saving & Loading**
   - Saved the trained **Linear Regression** model as a `.pkl` file using `joblib`.
   - Reloaded it for prediction without retraining.

4. **Streamlit Web App**
   - Built a simple, interactive web interface (`app.py`) using **Streamlit**.
   - Users can input housing features and get **predicted house prices** in real-time.

---

## 🧠 Tech Stack
- **Language:** Python 3  
- **Libraries:** Scikit-Learn, Pandas, NumPy, Streamlit, Joblib  
- **IDE/Environment:** VS Code

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository
bash

(https://github.com/abdulwaheedrrr/California-housing-dataset/upload/main)
cd california-housing-predictor
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run Streamlit App
bash
Copy code
streamlit run app.py
The app will open automatically in your browser. 🌐

📊 Model Performance
Model	R² Score
Linear Regression	0.67
Ridge Regression	0.67
Lasso Regression	0.66
Elastic Net	0.67

All models performed similarly, suggesting the dataset has limited nonlinear effects that linear models can capture.

🧩 Files Included
File	Description
model_train.py	Code for training all regression models
linear_model.pkl	Saved Linear Regression model
app.py	Streamlit web app for prediction
requirements.txt	All dependencies
README.md	Project documentation

💡 Future Improvements
Add non-linear models (Random Forest, XGBoost).

Perform feature engineering and hyperparameter tuning.

Visualize feature importance in the app.

👨‍💻 Author
Abdul Waheed
📧 [ab.wah876@gmail.com]
🌐 [https://github.com/abdulwaheedrrr]

⭐ If you like this project, please give it a star on GitHub! ⭐
