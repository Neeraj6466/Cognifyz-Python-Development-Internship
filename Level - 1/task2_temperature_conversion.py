
# Cognifyz Internship
# Level 1 - Task 2
# Temperature Conversion

print("Temperature Converter")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

temperature = float(input("Enter temperature: "))

if choice == "1":

    result = (temperature * 9/5) + 32

    print("Temperature in Fahrenheit:", result, "F")

elif choice == "2":

    result = (temperature - 32) * 5/9

    print("Temperature in Celsius:", result, "C")

else:

    print("Invalid choice! Please select 1 or 2.")