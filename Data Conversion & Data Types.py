# Data Conversion & Data Types
num_char = (input("Type a two digit number:\n"))
#Grabbing the input from the user in this case the numbers
nc_0 = ( num_char [0])
nc_1 = ( num_char [1])
# Converting the data type we grabbed from STR to INT
new_nc_0 = int (nc_0)
new_nc_1 = int (nc_1)
# add the data types together
num_add = new_nc_0 + new_nc_1
#convert back the int to a STR for printout
num_total = str (num_add)
#total printed here
print(num_total)