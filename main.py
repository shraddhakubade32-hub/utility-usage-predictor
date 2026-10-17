#Electicity usage prediction
print("Utility Usage Prediction Tool")
print("WelCome to my first project!")
print("purpose: Predict future electricity usage")

usage=150
usage = float(input("Enter your electicity usage in kWh: "))
print("Your recorded usage is:", usage,"kWh")

'''the formula we used
  Estimated Bill= Usage * Rate
'''
rate = 8
bill = usage * rate 
print("Estimated electricity bill:Rs.",bill)

# Store historical electricity usage
usage_records =[120,135,145,150,145]
print("Historical Electricity Usage:")
print(usage_records)

# Calculate average electricity usage
total_usage = sum(usage_records)
number_of_records = len(usage_records)
average_usage = total_usage/number_of_records

print("Total Electricity Usage:", total_usage,"kWh")
print("Number of Records:",number_of_records)
print("Average Electriciy Usage:",average_usage,"kWh")

# Find highest and lowest electricity usage
highest_usage = max(usage_records)
lowest_usage = min(usage_records)
print("Highest Electricity Usage:",highest_usage,"kWh")
print("Lowest Electricity Usage:",lowest_usage,"kWh")

#Display daily electricity usage
print("\n Daily Electricity Usage:")
for day, usage_value in enumerate(usage_records, start=1):
    print("Day",day, ":", usage_value,"kWh")

# Classify elecriciy usage
print("\nElectricity Usage Classification:")

for day, Usage_value in enumerate(usage_records, start=1):
    if usage_value >= 145:
        print("Day", day,":",usage_value,"kWh - High Usage")
else:
    print("Day",day,":",usage_value,"kWh - Normal Usage")

import pandas as pd
# Read the electricity data from CSV
data = pd.read_csv("m1.csv")

print("\n electricity Dataset:")
print(data)
print("\nFirst  10 Records:")
print(data.head(10))

#prepare data for Machine Learning
x = data[["DAY"]]
y = data["Usage_kWh"]
print("\nInput Data (x):")
print(x)
print("\nOutput Data (y)")
print(y)

from sklearn.linear_model import LinearRegression
#create the machine learning model
model =LinearRegression()
#train the model using historical data
model.fit(x,y)
print("\nMachine Learning Model Trained Successfully!") 

# Prediict electricity usage for a future day
try:
   future_day = int(input("\nEnter the number to predict usages:"))
   if future_day < 1:
       print("Please enter a day number greater than 0.")
   else:    
     prediction = model.predict([[future_day]])
     predicted_usage = round(prediction[0],2)

     rate = 8
     estimated_bill = predicted_usage* rate
     print("\n===== PREDICTION REPORT =====")
     print("Day Number:",future_day)
     print("Predicted Usage:",predicted_usage,"kWh")
     print("Estimated Bill:Rs.",round(estimated_bill, 2))
     print("========================")

except ValueError:
    print("Invalid input! Please enter a whoe number, such as 11.")

#Compare prediction with historical average
print("\n--- Usage Analysis ---")
print("Historical Average:",round(y.mean(),2),"kWh")
print("Prediction Usage :",round(prediction[0],2),"kWh" )

if prediction[0]>y.mean():
    print("Analysis:Usage is above the historical average.")
elif prediction[0]<y.mean():
    print("Analysis:Usage is below the historical average.")
else:
    print("Analysis:Usage is equal the historical average.")

