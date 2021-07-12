import datetime

#User input 2 dates, find their difference

user_input1_year = input("Enter the year of the first variable")
user_input1_month = input("Enter the month of the first variable")
user_input1_date = input("Enter the date of the first variable")

user_input2_year = input("Enter the year of the second variable")
user_input2_month = input("Enter the month of the second variable")
user_input2_date = input("Enter the date of the second variable")

date1 = datetime.date(int(user_input1_year),int(user_input1_month),int(user_input1_date))
date2 = datetime.date(int(user_input2_year),int(user_input2_month),int(user_input2_date))

date_diff = date2-date1

print("Difference between date1: " + str(date1) + " and date2: " + str(date2) + " is " + str(date_diff.days))

#User input birthday - find age. Today's date = datetime.date.today()
#User input date. Find if it is a leap year.