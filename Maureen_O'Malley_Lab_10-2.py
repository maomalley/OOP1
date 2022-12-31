#This program will ask for a string and return the letter(s) that
#occur most often.
def main():
    #Counter is imported to find all letters in a string.
    from collections import Counter
    #The program asks for a string.
    string = input("Enter a string: ")
    #Spaces will not be counted and lower/upper case will be treated the same.
    count = Counter(list(string.replace(' ','').lower()))
    max_freq = max(count.values())
    #Determines if two or more characters occur most frquently.
    letters = [letter for letter in count if count[letter] == max_freq]
    #The entered string is displayed.
    print("Your string is:",string)
    #This message is formatted to show more than one character if it appears.
    msg = "This character appears the most: {}. It appears {} times."
    print(msg.format(','.join(letters), max_freq))
main()
