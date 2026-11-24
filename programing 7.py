# Data Cleaning and Exploratory Data Analysis using Pandas
import pandas as pd

while True:
    try:
        count = int(input("How many records? "))
        if count > 0:
            break
        print("Enter a number greater than zero.")
    except ValueError:
        print("Please enter a whole number.")

names = []
departments = []
attendance_values = []
mark_values = []

for number in range(1, count + 1):
    print(f"\nRecord {number}")
    names.append(input("Name: ").strip())
    departments.append(input("Department: ").strip())

    # Blank attendance is treated as a missing value.
    while True:
        attendance_text = input("Attendance (leave blank if missing): ").strip()
        if attendance_text == "":
            attendance_values.append(None)
            break
        try:
            attendance_values.append(float(attendance_text))
            break
        except ValueError:
            print("Enter a number or leave blank.")

    # Blank mark is treated as a missing value.
    while True:
        mark_text = input("Mark (leave blank if missing): ").strip()
        if mark_text == "":
            mark_values.append(None)
            break
        try:
            mark_values.append(float(mark_text))
            break
        except ValueError:
            print("Enter a number or leave blank.")

data = {
    "Name": names,
    "Department": departments,
    "Attendance": attendance_values,
    "Mark": mark_values,
}

df = pd.DataFrame(data)
print("--- Original Dataset ---")
print(df)
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values using each column's mean.
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())

# Remove duplicate records.
df = df.drop_duplicates()
print("\n--- Cleaned Dataset ---")
print(df)
print("\n--- Descriptive Statistics ---")
print(df.describe())
print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))
print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))
