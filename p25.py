# Conditional statements with multiple conditions
age = int(input("Enter your age: "))
if age >= 18 and age <= 60:
    print("You are an adult")
elif age > 60:
    print("You are a senior citizen")
else:
    print("You are a minor")