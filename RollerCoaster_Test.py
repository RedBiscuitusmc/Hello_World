#Coding BootCamp Challenge Udemy
#Section 3
#RollerCoaster Testing
#Jacob Merlin

#opening message
print("Welcome to the rollercoaster!")
##Input request from the user
height = int(input("What is your height in cm?\n"))
bill = 0


if height >= 120:
    print ("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    #If statement
    if age < 12:
        #this varible tracks amount
        bill = 5
        print("Children tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    # using a logical operator to act as a catch all.
    elif age >= 45 and age <= 55:
        print("Everything is ok have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    #requesting user input
    wants_Photo = input("Do you want a photo taken? Y or N.\n")

    if wants_Photo == "Y":
        #adding varible to itself plus the amount which is $3
        bill =  bill + 3
        print("Photos are $3.")
    elif wants_Photo == "N":
        print("Ok thank you.")


else:
    print("Sorry, you have to grow taller before you can ride.")

print (f"Your total bill is ${bill}.")