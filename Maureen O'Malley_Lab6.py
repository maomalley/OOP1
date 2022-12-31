#To create the desired pattern, the number six is assigned
#to the steps variable.
steps = 6

#Nested loops are used to display the step-like pattern by
#using appropriate spaces and displaying pound signs.
for row in range(steps):
    print("#", end="")
    for column in range(row):
        print(" ", end="")
    print("#")
