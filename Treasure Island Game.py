#Coding BootCamp Challenge Udemy
#Section 3 Final
#Treasure Island Challenge
#Jacob A. Merlin

########################################################
print ('''
              ,.  _~-.,               .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'

~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^
''')

########################################################

#opening message
print("Welcome to Treasure Island!")
print("Your mission is to find treasure!")

########################################################
##Input request from the user
choice_1 = input("Your at a cross road. Where do you want to go? Type 'left' or 'right'\n")

########################################################
#Varbiles lower_case_choice_1 = l_c_choice_1
l_c_choice_1 = choice_1.lower()


########################################################
#If statement for controlling choices
if l_c_choice_1 == "left":
    print("You walked the left path, their is a lake at the end.")
    ########################################################
    ## Input request from the user
    choice_2 = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or Type 'swim' to swim across.\n")
    l_c_choice_2 = choice_2.lower()
    if l_c_choice_2 == "wait":
        print("You cross the lake safetly on the boat and arrive at the island and find three doors.")
        ########################################################
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? Type 'red' for red, 'blue' for blue and 'yellow' for yellow\n")
        l_c_choice_3 = choice_3.lower()
        if l_c_choice_3 == "yellow":
            print("You found the treasure, mission complete!!!!!!")
        elif l_c_choice_3 == "red":
            print("You get burned by fire. Game Over.")
        elif l_c_choice_3 == "blue":
            print("You get eaten by kittens. Game Over.")
    ########################################################
    elif l_c_choice_2 == "swim":
        print("You couldn't wait and where attacked by a trout. Game Over")


# End game Choice
elif l_c_choice_1 == "right":
    print("You took the right path and died. Game Over")
########################################################