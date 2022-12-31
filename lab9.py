def main():
    answer_key=['A', 'B', 'A', 'D', 'A',
                'C', 'C', 'D', 'B', 'C',
                'C', 'A', 'A', 'B', 'D',
                'A', 'B', 'C', 'D', 'B']
    student=[]
    correct=0
    incorrect=0
    
    infile = open('student.txt', 'r')
    student = infile.readlines()
    infile.close()

    index = 0

    print("Q\tocrr\tYour\tStatus")
    while index < 20:                 
        print(str(index+1) + "\t" + answer_key[index]+ "\t" + student[index],end="\t" )
    if student[index] == answer_key[index]:
        correct += 1
        index += 1
        print("Correct")
    else:
        incorrect += 1
        index += 1
        print("Wrong")
main()
