#This program will estimate the number of gallons of paint required,
#the hours of labor required, the cost of the paint, the labor charges
#and the total cost of the paint job given that every 112 square feet
#of wall space requires one gallon of paint and eight labor hours.

def main():
    #The program first asks for the square feet and price per gallon.
    sqft = int(input("Enter the square feet of wall space: "))
    gallons = int(input("Enter the paint's price per gallon: "))
    
    #The paint required was defined in a different function.
    print("Gallons of paint required:",format(requiredPaint(sqft), '.2f'))
    
    print("Hours of labor required:",format(requiredLabor(sqft), '.2f'))

    paintCost = requiredPaint(sqft) * gallons
    print("The cost for paint will be: $",format(paintCost, '.2f'))

    #One labor hour costs $35.
    laborCost = requiredLabor(sqft) * 35
    print("The cost for labor will be: $",format(laborCost, '.2f'))

    totalCost = paintCost + laborCost
    print("The total for this paint job is: $",format(totalCost, '.2f'))

#This function accepts the square feet to calculate required paint.
def requiredPaint(sqft):
    requiredPaint = sqft / 112
    return requiredPaint

#This function accepts the square feet to calculate the required labor.
def requiredLabor(sqft):
    requiredLabor = requiredPaint(sqft) * 8
    return requiredLabor

main()
