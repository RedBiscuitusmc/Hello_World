#BMI Calculator
#Section 2 code challenge
#request information from user
height = input("enter your height in meters: ")
weight = input("enter your weight in kg: ")
#handle conversion
new_height = float (height)
new_weight = int (weight)
#math
result = new_weight / new_height ** 2
#handle conversion
bmi_result = int(result)
#send back user data
print(bmi_result)