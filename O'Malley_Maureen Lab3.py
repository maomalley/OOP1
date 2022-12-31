#Write a program that prompts the user to enter a number within the range of 1
#through 10. The program should display the Roman numeral version of that
#number  If the number is outside the range of 1 through 10, the program
#should display an error message.

#The user will be prompted to enter a number between 1-10 which is assigned
#to the variable "number".
number = int(input("Enter any number in the range 1 through 10 : "))

#If any number 1-10 is entered, the correct numeral will be returned
#through the use of the following if-elif-else statement:
if number == 1:
    print("The Roman numeral for 1 is I." )
elif number == 2:
    print("The Roman numeral for 2 is II." )
elif number == 3:
    print("The Roman numeral for 3 is III." )
elif number == 4:
    print("The Roman numeral for 4 is IV." )
elif number == 5:
    print("The Roman numeral for 5 is V." )
elif number == 6:
    print("The Roman numeral for 6 is VI." )
elif number == 7:
    print("The Roman numeral for 7 is VII." )
elif number == 8:
    print("The Roman numeral for 8 is VIII." )
elif number == 9:
    print("The Roman numeral for 9 is IX." )
elif number == 10:
    print("The Roman numeral for 10 is X." )

#Following the if-elif statements, the else statement occurs if a number
#outside of 1-10 is entered.
else:
    print("ERROR: A number between 1 - 10 was not entered.")
