#This program will let the user enter a course number, then it will
#display the course's room number, instructor and meeting time.
def main():
    #This dictionary contains room numbers for each course.
    room = {
        "CS101":3004,
        "CS102":4501,
        "CS103":6755,
        "NT110":1244,
        "CM241":1411
    }
    #This dictionary contains instructor names for each course.
    instructor = {
        "CS101":"Haynes",
        "CS102":"Alvarado",
        "CS103":"Rich",
        "NT110":"Burke",
        "CM241":"Lee"
    }
    #This dictionary containes the times each course will start at.
    time = {
        "CS101":"8:00 a.m.",
        "CS102":"9:00 a.m.",
        "CS103":"10:00 a.m.",
        "NT110":"11:00 a.m.",
        "CM241":"1:00 p.m."
    }
    #The user will enter a course number to obtain more information.
    course = input("Enter a course number for more information: ")
    #Different dictionary values will be pulled depending on the course number.
    if course == "CS101":
        print("Room number:",room["CS101"])
        print("Instructor:",instructor["CS101"])
        print("Starts at:",time["CS101"])
    elif course == "CS102":
        print("Room number",room["CS102"])
        print("Instructor:",instructor["CS102"])
        print("Starts at:",time["CS102"])
    elif course == "CS103":
        print("Room number",room["CS103"])
        print("Instructor:",instructor["CS103"])
        print("Starts at:",time["CS103"])
    elif course == "NT110":
        print("Room number",room["NT110"])
        print("Instructor:",instructor["NT110"])
        print("Starts at:",time["NT110"])
    elif course == "CM241":
        print("Room number",room["CM241"])
        print("Instructor:",instructor["CM241"])
        print("Starts at:",time["CM241"])
    #This occurs if the user does not enter a course in the dictionary.
    else:
        print("Valid courses are CS101, CS102, CS103, NT110 or CM241")
main()
