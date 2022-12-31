#This program displays the total of the values in numbers.txt:
#1, 2, 4, 5, 7, 8, 12, 15, 18, 27, 38, 78, 152

def main():
    #Initialize an accumulator
    total = 0.0

    try:
        #numbers.txt is opened and assigned to a variable
        infile = open('numbers.txt','r')
        
        #Values are read, accumulated and then displayed.
        for line in infile:
            amount = float(line)
            total += amount
            numbers = int(line)
            print(numbers)

        #Close the file.
        infile.close()
    except Exception as err:
        print(err)
    else:
        #Display the total.
        print("The total is:", format(total,'.2f'))

main()
