#The program asks the number of packages purchased.
packages = int(input("Enter the number of packages purchased: "))

#The packages variable will be used in the following if-elif-else
#statement to determine what discount can be applied to it.
if 10 <= packages and packages <= 19:
	origionalCost = packages * 99        #Each package costs $99.
	discount = origionalCost * .10       #A 10% discount can be applied.
	amountDue = origionalCost - discount #The discount is taken off.
	print("The original cost was: $"+str(format(origionalCost, ',.2f')))
	print("The amount saved is: $"+str(format(discount, ',.2f')))
	print("The total comes to: $"+str(format(amountDue, ',.2f')))

#A higher discount is applied if the user buys more product.
elif 20 <= packages and packages <= 49:
	origionalCost = packages * 99
	discount = origionalCost * .20
	amountDue = origionalCost - discount
	print("The original cost was: $"+str(format(origionalCost, ',.2f')))
	print("The amount saved is: $"+str(format(discount, ',.2f')))
	print("The total comes to: $"+str(format(amountDue, ',.2f')))
	
#The discount and amountDue are formatted so they display two decimals.
elif 50 <= packages and packages <= 99:
	origionalCost = packages * 99
	discount = origionalCost * .30
	amountDue = origionalCost - discount
	print("The original cost was: $"+str(format(origionalCost, ',.2f')))
	print("The amount saved is: $"+str(format(discount, ',.2f')))
	print("The total comes to: $"+str(format(amountDue, ',.2f')))
	
#This last range includes all numbers that are 100 or higher.
elif packages >= 100:
	origionalCost = packages * 99
	discount = origionalCost * .40
	amountDue = origionalCost - discount
	print("The original cost was: $"+str(format(origionalCost, ',.2f')))
	print("The amount saved is: $"+str(format(discount, ',.2f')))
	print("The total comes to: $"+str(format(amountDue, ',.2f')))

#The else statement occurs if less than 10 packages were purchased.	
else:
	origionalCost = packages * 99
	print("No discounts are applicable.")
	print("The total comes to: $"+str(format(origionalCost, ',.2f')))
