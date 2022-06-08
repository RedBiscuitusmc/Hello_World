#Coding BootCamp Challenge Udemy
#Section 3
#Odd OR Even code challenge
#Jacob Merlin


print("Welcome to is it odd or even?")
#Input request from user
number = int(input("Which number do you want to check?\n "))

#Checking if the number is odd or even value
check_Num = number % 2

#If statement
if check_Num <= 0 :
    print("This is an even number.")
else :
    print("This is an odd number.")
