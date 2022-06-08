#Coding BootCamp Challenge Udemy
#Section 2.26
#Tip Calculator
#Jacob Merlin

message_Opener = "Welcome to the tip calculator\n"
print(message_Opener)

#Input for bill amount
total_Bill = input("What was the total bill?\n")
# tp= tip percentage
tp_Bill = input("What percentage tip would you like to give? 10, 12, or 15?\n")
#TPA = total amount of people to split the bill
tpa_Bill = input("How many people to split the bill?\n")

#Converting age input from str to int bill_ct = converted total
# bill_ct = total bill bill_ctp = total percent bill bill_ctpa = how many people split the bill
bill_ct = float(total_Bill)
bill_ctp = int(tp_Bill)
bill_ctpa = int(tpa_Bill)
#Using varibles we define how the math comes together to get our total sum
# the percent for the total amount of the bill / the percent  12/100 = 0.12
bill_Percent = bill_ctp / 100
#Running the bill amount against the percent
bill_P_T = round (bill_ct * bill_Percent, 2)
#Taking that new total to get the new whole amount
total_bct = bill_P_T + bill_ct
#Breaking down the whole amount into how much each person pays
split_Total = round (total_bct / bill_ctpa, 2)
#Final output displayed
message_Close =  f"Each person should pay: {split_Total} "
print (message_Close)
