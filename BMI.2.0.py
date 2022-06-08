#Coding BootCamp Challenge Udemy
#Section 3
#BMI Calculator 2.0
#Jacob Merlin


height = input("enter your height in meters: ")
weight = input("enter your weight in kg: ")
#handle conversion
new_height = float (height)
new_weight = int (weight)
#math
result = round (new_weight / new_height ** 2)
#handle conversion
bmi_result = int(result)

if result <= 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif result <= 25:
    print(f"Your BMI is {result}, you have a normal weight.")
elif result <= 30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif result <= 35:
    print(f"Your BMI is {result}, you are obese.")
else :
    print(f"Your BMI is {result}, you are clinically obese.")