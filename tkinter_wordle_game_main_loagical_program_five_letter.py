from argparse import _CountAction
from operator import length_hint
import random

global tmpAnswer
global tmpRandomChoice
global listAns
global countC
global countI
global listUserAns
global finalWord
chanceCount=1

class WordleClass:
    def __init__(self):
        print("Hello, this is class mysqlCon from file testdbfile...")


    def getNewFinalWord():
        global listAns
        global tmpRandomChoice
        global listFinal
        #This code is to get final word list from file.
        listAns=[]
        file=open("C:\\Users\ma29h\Downloads\wordle.txt","r")
        str=file.read().split('\n')

        listAns=str
        file.close()
        print(listAns)
        #End of the code.

        #Generating random number's word for today's game.
        tmpRandomChoice=random.randrange(0,4)

        #This to store random generated word for Game.
        i=1
        global finalWord
        finalWord=listAns[tmpRandomChoice]
        global listFinal
        listFinal=[]
        listFinal.clear()
        for i in range(5):
            listFinal.append(finalWord[i])
            print(listFinal)
        return finalWord

    def getCorrectAnswer():
        global finalWord
        print(f"Correct Answer = {finalWord}")
        return finalWord



    def fnStoreUserInputList(tmpAnswer):
        #Here, starting the storing user input in list from here.
        global listFinal
        global listUserAns
        listUserAns=[]
        listUserAns.clear()
        j=1
        for j in range(5):
            listUserAns.append(tmpAnswer[j])
            print(listUserAns)

        #Matching User and Final Answer.
        global countC
        global countI

        #This list to be used to make TKINTER UI , green-yellow-grey as per the answer.
        global greenList
        global yellowList
        global greyList

        greenList = []
        yellowList = []
        greyList = []
        #-------------End ------------.

        countC=0
        countI=0
        k=0
        l=0

        #
        for k in range(5):
            print(f"\nChecking result for the #{k+1} letter.")
            flag1=0
            flag2=0
            flag3=0
            for l in range(5):
                user=listUserAns[k]
                computer=listFinal[l]

                #user==compter is used for letter matching, k==l is used for position matching.
                if user==computer and k==l:
                    flag1=1
                elif user==computer and k!=l:
                    flag2=2
                elif user!=computer:
                    flag3=3
                else:
                    print("")

            if flag1==1 and flag3==3:
                #print(f"Position of letter #{user} is correct.")
                print(f"\033[1;32;40m {user}  \n")
                countC+=1
                greenList.append(k+1)
            elif flag2==2 and flag3==3:             
                #print(f"This #{user} letter is exist but position is not correct.")
                print(f"\033[1;33;40m {user}  \n")
                countI+=1
                yellowList.append(k+1)
            elif flag3==3:
                #print(f"This #{user} letter is not exist.")
                print(f"\033[1;37;40m {user}  \n")
                countI+=1
                greyList.append(k+1)
            else:
                print("")
        
        #Calling function to check final answer and user limits.
        return greenList, yellowList, greyList


        #Function to check maximum limit to get answer from user if user is wrong.
        #Function calling for user input and it's length validation.