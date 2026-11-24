import pandas as pd

names = []
departments = []
mark_values = []

for number in range(1, 6):
    print(f"\nStudent {number}")
    names.append(input("Name: ").strip())
    departments.append(input("Department: ").strip())

    while True:
        try:
            mark_values.append(float(input("Mark: ")))
            break
        except ValueError:
            print("Please enter a number for the mark.")

marks = pd.Series(mark_values, index=["A", "B", "C", "D", "E"])

print("--- Pandas Series ---")
print(marks)

data = {
    "RollNo": [101, 102, 103, 104, 105],
    "Name": names,
    "Department": departments,
    "Mark": mark_values,
}

df = pd.DataFrame(data)
print("\n--- DataFrame ---")
print(df)
print("\nAverage Mark:", round(df["Mark"].mean(), 2))
print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])