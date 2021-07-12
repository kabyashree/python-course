#User input 3 numbers. Find the largest number, smallest number. Print the sum, average, squares of the numbers
#User input 2 numbers. Options - add, multiply, divide, subtract using options as user input.

number1 = int(input('Enter First number : '))
number2 = int(input('Enter Second number : '))
number3 = int(input('Enter third number : '))

def largest(num1, num2, num3):
    if (num1 > num2) and (num2 > num3):
        largest_num = num1
    elif (num2 > num1) and (num2 > num3):
        largest_num = num2
    else:
        largest_num = num3
        print("The largest of the 3 numbers is : ", largest_num)
    return

def smallest(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        smallest_num = num1
    elif (num2 < num1) and (num2 < num3):
        smallest_num = num2
    else:
        smallest_num = num3
        print("The smallest of the 3 numbers is : ", smallest_num)
    return

largest(number1, number2, number3)
smallest(number1, number2, number3)

#user_input = "Enter 1 to add, 2 to multiply.....")
#if user_input == "1": print add.....