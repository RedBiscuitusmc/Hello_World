#Coding BootCamp Challenge Udemy
#Section 3
#Control Oprations
#Jacob Merlin

print("Welcome to the rollercaoster!")
#Input Request
height = int (input("What is your height in cm?\n"))

#IF Statement
if height >= 120:
    print("You can ride the rollercoaster")
    age = int (input("What is your age?\n"))
    if age <= 12:
        print("Please pay $5")
    elif age <= 18:
        print("Your Ticket costs $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride.")