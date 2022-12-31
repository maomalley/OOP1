#The program asks the number of packages purchased.
packages = int(input("Enter the number of packages purchased: "))

#The packages variable will be used in the following if-elif-else
#statement to determine what discount can be applied to it.
if 10 <= packages and packages <= 19:
	purchase = packages * 99        #Each package costs $99.
	discount = purchase * .10       #A 10% discount can be applied.
	amountDue = purchase - discount #The discount is taken off.
	print("A 10% discount has been applied.")
	print("The amount saved is: $"+str(format(discount, ',.2f')))
	print("The total comes to: $"+str(format(amountDue, ',.2f')))

#A higher discount is applied if the user buys more product.
elif 20 <= packages and packages <= 49:
	purchase = packages * 99
	discount = purchase * .20
	amountDue = purchase - discount
	print("A 20% discount has been applied.")
	print("The amount saved is: $"+str(format(discount, ',.2f')))
	print("The total comes to: $"+str(format(amountDue, ',.2f')))
	
#The discount and amountDue are formatted so they display two decimals.
elif 50 <= packages and packages <= 99:
	purchase = packages * 99
	discount = purchase * .30
	amountDue = purchase - discount
	print("A 30% discount has been applied.")
	print("The amount saved is: $"+str(format(discount, ',.2f')))
	print("The total comes to: $"+str(format(amountDue, ',.2f')))
	
#This last range includes all numbers that are 100 or higher.
elif packages >= 100:
	purchase = packages * 99
	discount = purchase * .40
	amountDue = purchase - discount
	print("A 40% discount has been applied.")
	print("The amount saved is: $"+str(format(discount, ',.2f')))
	print("The total comes to: $"+str(format(amountDue, ',.2f')))

#The else statement occurs if less than 10 packages are purchased.	
else:
	purchase = packages * 99
	print("No discounts are applicable.")
	print("The total comes to: $"+str(format(purchase, ',.2f')))
