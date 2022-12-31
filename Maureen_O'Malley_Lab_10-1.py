#This program asks for a string containing a first, middle and last name.
#These names are converted into initials and displayed.
#If the user enters "NA" as a middle name, only the first and last will appear.

def main():
    #Asks for a string containing a fist, middle and last name.
    string = input("Enter your first, middle and last names: ")    
    name = string.split()

    #The program deletes the middle name if it is NA.
    if "NA" in name:
        del name[1]

    for ch in name:
        print(ch[0] + ".", end=" ")
    print()

main()
