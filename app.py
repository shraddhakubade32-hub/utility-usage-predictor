import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


def load_data():
    data = pd.read_csv("m1.csv")
    required_columns = ["Day", "Usage_kWh"]

    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing column: {column}")

    # Convert values to numbers
    data["Day"] = pd.to_numeric(data["Day"], errors="coerce")
    data["Usage_kWh"] = pd.to_numeric(
        data["Usage_kWh"], errors="coerce"
    )

    # Remove invalid records
    data = data.dropna(subset=["Day", "Usage_kWh"])

    data = data[
        (data["Day"] >= 1) &
        (data["Usage_kWh"] >= 0)
    ].copy()

    if len(data) < 2:
        raise ValueError("At least 2 valid records are required.")

    X = data[["Day"]]
    y = data["Usage_kWh"]

    print("Valid records:", len(data))

    return X, y


def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model
def evaluate_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    error = mean_absolute_error(y_test, predictions)

    print("\n===== MODEL EVALUATION =====")
    print("Mean Absolute Error:", round(error, 2), "kWh")
    print("============================")

def predict_usage(model, y):
    try:
        future_day = int(
            input("Enter the day number to predict usage: ")
        )

        if future_day < 1:
            print("Please enter a positive day number.")
            return

        prediction = model.predict(
            pd.DataFrame({"Day": [future_day]})
        )

        predicted_usage = round(float(prediction[0]), 2)

        rate = 8
        estimated_bill = predicted_usage * rate

        print("\n===== PREDICTION REPORT =====")
        print("Day Number:", future_day)
        print("Predicted Usage:", predicted_usage, "kWh")
        print("Estimated Bill: Rs.", round(estimated_bill, 2))
        print("=============================")

        historical_average = float(y.mean())
        print("Historical Average:",
              round(historical_average, 2), "kWh")

        difference = predicted_usage - historical_average

        if difference > 0:
            print("Usage Status: Above historical average")
        elif difference < 0:
            print("Usage Status: Below historical average")
        else:
            print("Usage Status: Equal to historical average")

    except ValueError:
        print("Invalid input! Enter a whole number, such as 11.")
def plot_usage(X, y, model):
    plt.scatter(X["Day"], y, label="Actual Usage")

    plt.plot(
        X["Day"],
        model.predict(X),
        color="red",
        label="Predicted Usage"
    )

    plt.xlabel("Day")
    plt.ylabel("Electricity Usage (kWh)")
    plt.title("Electricity Usage Prediction")
    plt.legend()
    plt.grid(True)
    plt.savefig("usage_prediction.png")
    plt.show()


def main():
    X, y = load_data()
    model = train_model(X, y)

    evaluate_model(X, y)

    print("\nUtility Usage Prediction Tool")
    print("Model trained successfully!")

    predict_usage(model, y)
    plot_usage(X, y, model)


if __name__ == "__main__":
    main()
