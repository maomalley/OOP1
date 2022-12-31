#This program will return a user's initials

def main():
    firstName = input("Enter your first name: ")

    middleName = input("Enter your middle name or \"NA\" if none: ")
    
    lastName = input("Enter your last name: ")

    if middleName == "NA":
        print("Your initials are: ",firstName[0],".",lastName[0],".",sep="")
    else:
        print("Your initials are: ",firstName[0],".",middleName[0],".",lastName[0],".",sep="")
main()
