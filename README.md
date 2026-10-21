# Utility Usage Prediction Tool

# About the Project
This is my beginner Machine Learning project, created to learn how Linear Regression works using Python.
The project uses daily electricity usage data from a CSV file to train a model and predict the estimated usage for a given day. It also shows a graph to help understand the usage pattern.

# Features
- Reads electricity usage data from a CSV file.
- Trains a Linear Regression model.
- Predicts usage for a given day.
- Checks model performance using Mean Absolute Error (MAE).
- Displays a graph of actual usage and the regression line.
- Estimates the electricity bill using a sample rate of ₹8 per kWh.

# Technologies Used
- Python
- Pandas
- Scikit-learn
- Matplotlib

# Project Files
- `app.py` – Main Python program.
- `main.py` – Additional Python file.
- `m1.csv` – Electricity usage dataset.
- `requirements.txt` – Required Python libraries.
- `usage_prediction.png` – Generated usage graph.

## How to Run the Project

1. Clone the repository
```bash
git clone https://github.com/shraddhakubade32-hub/utility-usage-predictor.git
```

2. Open the project folder
```bash
cd utility-usage-predictor
```

3. Install the required libraries
```bash
pip install -r requirements.txt
```

4. Run the program
```bash
python app.py
```

Follow the instructions displayed in the terminal.

# Dataset

The file `m1.csv` contains two columns:

- `Day` – Day number.
- `Usage_kWh` – Electricity usage in kilowatt-hours.

The current dataset contains sample values for learning and testing.

# What I Learned

While working on this project, I practised using Python libraries, loading CSV data, training a Linear Regression model, evaluating predictions, and plotting a graph.

# Future Improvements

- Use more electricity usage data.
- Include other factors such as temperature and weather.
- Try other Machine Learning algorithms.
- Improve prediction accuracy with more suitable data.

# About Me

**Shraddha Kubade**

Electronics and Telecommunication Engineering Student | Learning AI and Machine Learning

# Note

This project is for learning purposes. The dataset and electricity rate are examples, so the predictions and estimated bills may not match actual electricity usage or charges.
