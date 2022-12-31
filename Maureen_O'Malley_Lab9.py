def main():
    #The answers are stored into a list.
    answerKey = ["A", "B", "A", "D", "A",
                 "C", "C", "D", "B", "C",
                 "C", "A", "A", "B", "D",
                 "A", "B", "C", "D", "B"]
    user_answers = []

    #The student's answers are read and stored into a list.
    infile = open('user_answers.txt', 'r')
    for i in infile.readlines():
        j = i.rstrip("\n")
        user_answers.append(j)
    infile.close()

    #This lists shows which answers were correct or incorrect.
    index = 0
    print("#\tAns.\tValidity\n--------------------------")
    while index < 20:
        print(str(index+1) + "\t" + user_answers[index],end="\t")
        if user_answers[index] == answerKey[index]:
            index += 1
            print("Correct")
        else:
            index += 1
            print("Incorrect")
    
    #The total number of correct answers is displayed.
    i = 0
    j = 0
    for k in range(len(answerKey)):
        if(answerKey[k] == user_answers[k]):
            i += 1
        else:
            j += 1
    print("Correct answers:",i,"out of",len(answerKey))
    #The total number of incorrect answers is displated.
    print("Incorrect answers:",j,"out of",len(answerKey))
    #The student needs 15 correct answers to pass.
    if i >= 15:
        print("You've passed!")
    else:
        print("You did not pass.")
main()
