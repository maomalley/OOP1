#Write a Program that displays the following information:
#Your name
#Your address, with city, state, and ZIP
#Your telephone number
#Your college major

#The program will first ask for a name, address, phone number and major.
name = input("What is your name? ")                     #Assigning user's name
city = input("What is your city's name? ")              #Assigning address 
state = input("What is your state? ")                   #Assigning state
zipCode = input("What is your ZIP code? ")              #Assigning ZIP
telephoneNumber = input("What is your phone number? ")  #Assigning phone number
collegeMajor = input("What is your college major? ")    #Assigning college major

#The program will display the entered name, address, phone number and major.
print("Your name: ",name)                               #Displaying user's name
print("Your address: "+city+", "+state+", "+zipCode)    #Displaying address
print("Your phone number: ",telephoneNumber)            #Displaying phone number
print("Your college major: ",collegeMajor)              #Displaying major
