#Coding BootCamp Challenge Udemy
#Section 2.25
#Your life in weeks
age = input("What is your current age?\n")
days = 365
weeks = 52
months = 12
years = 90

#Converting age input from str to int
d_age = int(age)
#Using varibles we define how the math comes together to get our total sum
total_day_Age = d_age * days
days_Years = days * years
total_days = days_Years - total_day_Age
#repeated as from listed above
w_age = int(age)

total_week_Age = w_age * weeks
week_Years = weeks * years
total_weeks = week_Years - total_week_Age
#Repeated as from listed above
m_age = int(age)

total_month_Age = m_age * months
month_Years = months * years
total_month = month_Years - total_month_Age

#fstring
message =  f" You have {total_days} days, {total_weeks} weeks, {total_month} months left."
print (message)