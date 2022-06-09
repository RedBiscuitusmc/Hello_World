#Coding BootCamp Challenge Udemy
#Section 3
#Love Calculator
#Jacob Merlin

########################################################

#opening message
print("Welcome to the Love Calculator!")
##Input request from the user
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

########################################################
#true name 1
lower_case_name_1 = name1.lower()
#True lower case name count
count_T = lower_case_name_1.count("t")
count_R = lower_case_name_1.count("r")
count_U = lower_case_name_1.count("u")
count_E = lower_case_name_1.count("e")

#true love name 2
lower_case_name_2 = name2.lower()
#True lower case name count
count_T_2 = lower_case_name_2.count("t")
count_R_2 = lower_case_name_2.count("r")
count_U_2 = lower_case_name_2.count("u")
count_E_2 = lower_case_name_2.count("e")

total_true_count = count_T + count_R + count_U + count_E + count_T_2 + count_R_2 + count_U_2 + count_E_2
########################################################

#Love lower case name1 count
l_count_L = lower_case_name_1.count("l")
l_count_O = lower_case_name_1.count("o")
l_count_V = lower_case_name_1.count("v")
l_count_E = lower_case_name_1.count("e")

#true love name 2
lower_case_name_2 = name2.lower()
#Love lower case name count
count_L_2 = lower_case_name_2.count("l")
count_O_2 = lower_case_name_2.count("o")
count_V_2 = lower_case_name_2.count("v")
count_E_2 = lower_case_name_2.count("e")
#Total count for name 2
total_love_count = l_count_L + l_count_O + l_count_V + l_count_E + count_L_2 + count_O_2 + count_V_2 + count_E_2

########################################################

#total amount combined for both names
t_T_C = str (total_true_count)
t_L_C = str (total_love_count)
combined_Count = t_T_C + t_L_C
total_Score = int(combined_Count)

########################################################

if total_Score <= 10 or total_Score >= 90:
    print(f"Your score is {total_Score}, you go together like coke and mentos.")
elif total_Score >= 40 or total_Score <= 50:
    print(f"Your score is {total_Score}, you are alright together.")
else:
    print(f"Your score is {total_Score}.")