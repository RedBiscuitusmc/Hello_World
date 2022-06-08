#Coding BootCamp Challenge Udemy
#Section 3
#Leap Year 3.3
#Jacob Merlin

#Input request from the user
year = int(input("Which year do you want to check? "))

#math checking if year divdes into amount evenly to check for a leap year.
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("leap year.")

else:
    print("Not leap year")
