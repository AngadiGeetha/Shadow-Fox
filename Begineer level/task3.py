#1.program to determine the BMI Category based on user input
# Get user input
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

# Print results
print(f"\nYour BMI is: {bmi:.2f}")
print(f"BMI Category: {category}")

#program to determine which country a city belongs to
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"] 
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] 
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city=input("Enter a city name:")
if city in ["Sydney", "Melbourne", "Brisbane", "Perth"]:
    print(city +" "+"belongs to australia")
elif city in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]:
    print(city + " " +"belongs to UAE")
elif city in ["Mumbai", "Bangalore", "Chennai", "Delhi"]:
    print(city + " " + "belongs to India")
else:
    print ("city is not found")

#

