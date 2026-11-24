
# Cognifyz Internship
# Level 1 - Task 4
# Calculator Program

print("===== SIMPLE CALCULATOR =====")

# Get two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get operator
operator = input("Enter operator (+, -, *, /, %): ")

# Perform calculation
if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero")

elif operator == "%":
    if num2 != 0:
        result = num1 % num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operator!")
