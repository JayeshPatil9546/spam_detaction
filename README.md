# 📧 Spam Message Classifier

This project uses multiple machine learning algorithms to classify SMS messages as **spam** or **ham**. It demonstrates data preprocessing, model training, evaluation, and ensemble learning using stacking.

---

## 📂 Dataset

- File: `SPAM.csv`
- Contains 5572 messages labeled as `spam` or `ham`.
- Unnecessary columns were removed.
- Labels are encoded:  
  - `spam` → `0`  
  - `ham` → `1`

---

## 🔧 Requirements

Install the required packages using pip:

```bash
pip install numpy pandas matplotlib scikit-learn

🧠 Models Used
Logistic Regression

Decision Tree

K-Nearest Neighbors (KNN)

Random Forest

Stacking Classifier (SVM as final estimator)

📊 Evaluation Metrics
Each model was evaluated on:

Training Accuracy

Testing Accuracy

Precision

Recall

F1 Score

🔍 Sample Results
Model	Train Acc	Test Acc	Precision	Recall	F1 Score
LR	96.61%	96.23%	0.959	0.999	0.978
DT	100%	96.86%	0.976	0.987	0.981
KNN	91.99%	90.58%	0.901	1.000	0.948
RF	100%	97.76%	0.975	0.999	0.987
STACK	99.98%	98.65%	0.986	0.998	0.992
📈 Visualization
A comparison plot is created using matplotlib to visualize model performance across metrics.

✉️ Prediction Example
python
Copy
Edit
input_mail = ["Hi this is kalyan"]
input_features = feature_extraction.transform(input_mail)
prediction = stack.predict(input_features)

if prediction == 0:
    print("SPAM MAIL")
else:
    print("HAM MAIL")
Output:

nginx
Copy
Edit
HAM MAIL
