#One acre of land is equivalent to 43,560 square feet.
#Write a program that asks the user to
#enter the total square feet in a tract of land
#and calculates the number of acres in the tract.

#Ask for the total square feet of the land
squareFeet = int(input("Enter the number of total square feet in the tract: "))
#Calculate the total acres of the land
totalAcres = squareFeet / 43560

#Display the input in total acres
print("The total number of acres for that tract is: ",format(totalAcres,',.2f'))
