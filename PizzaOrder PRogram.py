#Coding BootCamp Challenge Udemy
#Section 3
#Pizza Order Program
#Jacob Merlin

#opening message
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L?\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

#Varible Tracks bill total
bill = 0

if size == "S":
    #Small Pizzas are $15
    bill = bill + 15
    ################################
    if add_pepperoni == "Y":
        #add pepperoni $2 for small
        bill = bill + 2
    ################################
################################
elif size == "M":
    #Medium Pizzas are $20
    bill = bill + 20
    ################################
    if add_pepperoni == "Y":
        #add pepperoni $3 for Medium / Large
        bill = bill + 3
    ################################
################################
elif size == "L":
    #Large Pizzas are $25
    bill = bill + 25
    ################################
    if add_pepperoni == "Y":
        #add pepperoni $3 for Medium / Large
        bill = bill + 3
    ################################
if extra_cheese == "Y":
    #Extra cheese is $1
    bill = bill + 1


print(f"Your total bill is ${bill}")