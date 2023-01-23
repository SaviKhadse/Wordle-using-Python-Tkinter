#import modules
from math import radians
from tkinter_dbconnection_file import mysqlCon
from cgitb import text
from tkinter import *
from tkinter import font
from tkinter import END, Label, messagebox

# This module provides a portable way of using operating system dependent functionality.
import os
from tkinter import messagebox
from operator import length_hint
import random

#Global Variable Declaration.
global tmpAnswer
global tmpRandomChoice

global tempCount  # This variable to call word to check as per the attempts.
tempCount = 1
global nextlevelframe

# importing database class from file name called "tkinter_dbconeection_file.py"
class WordleClass(mysqlCon):
    def __init__(self):
        print("Hello this is wordleclass...")
        self.fndbconn()

    def getNewFinalWord(self):
        global tmpRandomChoice
        # This code is to get final word list from file.
        self.listAns = []
        file = open("/Users/sagartandel/Documents/Sagar Study/OOPJ and Python/Final Version/wordle.txt","r")
        self.listAns = file.read().split('\n')
        file.close()
        
        # Generating random number's word for today's game.
        tmpRandomChoice = random.randrange(0, 25)

        # This to store random generated word for Game.
        i = 1
        self.finalWord = self.listAns[tmpRandomChoice]
        print(self.finalWord)

        self.listFinal = []
        self.listFinal.clear()
        for i in range(5):
            self.listFinal.append(self.finalWord[i])
        print(self.listFinal)
        return self.finalWord

    def getCorrectAnswer(self):
        print(f"Correct Answer = {self.finalWord}")
        return self.finalWord

    def fnStoreUserInputList(self, tmpAnswer):
        # Here, starting the storing user input in list from here.
        self.listUserAns = []
        self.listUserAns.clear()
        j = 1
        for j in range(5):
            self.listUserAns.append(tmpAnswer[j])
        print(self.listUserAns)

        # Matching User and Final Answer.
        # This list to be used to make TKINTER UI , green-yellow-grey as per the answer.
        global greenList
        global yellowList
        global greyList

        greenList = []
        yellowList = []
        greyList = []
        # -------------End ------------.

        self.countC = 0
        self.countI = 0
        k = 0
        l = 0

        # LOOP TO CHECK USERS WORD LETTER WITH COMPUTER GENERATED WORD LETTER
        for k in range(5):
            print(f"\nChecking result for the #{k+1} letter.")
            flag1 = 0
            flag2 = 0
            flag3 = 0
            for l in range(5):
                user = self.listUserAns[k]
                computer = self.listFinal[l]

                # user==compter is used for letter matching, k==l is used for position matching.
                if user == computer and k == l:
                    flag1 = 1
                elif user == computer and k != l:
                    flag2 = 2
                elif user != computer:
                    flag3 = 3
                else:
                    pass
            
            #Check and add answer in respective lists.
            if flag1 == 1:
                # print(f"Position of letter #{user} is correct.")
                print(f"\033[1;32;40m {user}  \n")
                self.countC += 1
                greenList.append(k+1)
            elif flag2 == 2 and flag3 == 3:
                # print(f"This #{user} letter is exist but position is not correct.")
                print(f"\033[1;33;40m {user}  \n")
                self.countI += 1
                yellowList.append(k+1)
            elif flag3 == 3:
                # print(f"This #{user} letter is not exist.")
                print(f"\033[1;37;40m {user}  \n")
                self.countI += 1
                greyList.append(k+1)
            else:
                pass

        # Calling function to check final answer and user limits.
        return greenList, yellowList, greyList

#This class is for Registration page.
class RegisterClass(mysqlCon):
    def register_user(self):        #Implementing event on register button.
        self.fndbconn()     #Calling fndbConn() from mysqlConn class using Inheritance.

        self.username_info = self.username.get()
        self.password_info = self.password.get()
        self.email_info = self.tmpemail.get()

        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.email_entry.delete(0, END)

        checkUser = mysqlCon.fnRegister(self.username_info, self.password_info, self.email_info)
        messagebox.showinfo(
            "Success!", "Welcome! Registration Done Suceessfully..")
        register_screen.destroy()

    # Designing window for registration
    def register(self):
        global register_screen
        register_screen = Toplevel(main_screen)
        register_screen.title("Register")
        register_screen.geometry("350x500")

        # Added for Wordle....
        iframe = Frame(register_screen)
        iframe.pack()

        topframe = Frame(register_screen)
        topframe.pack()

        mframe = Frame(register_screen)
        mframe.pack()

        L1 = Label(iframe, font=("Apple, 10"))
        L1.pack()

        L1 = Label(topframe, text="W", font=("Apple, 25"), bg="#8FDE21", width=2)
        L2 = Label(topframe, text="O", font=("Apple, 25"), bg="#8FDE21", width=2)
        L3 = Label(topframe, text="R", font=("Apple, 25"), bg="#8FDE21", width=2)
        L4 = Label(topframe, text="D", font=("Apple, 25"), bg="#8FDE21", width=2)
        L5 = Label(topframe, text="L", font=("Apple, 25"), bg="#8FDE21", width=2)
        L6 = Label(topframe, text="E", font=("Apple, 25"), bg="#8FDE21", width=2)
        L6.pack(side=RIGHT, padx=3, pady=10)
        L5.pack(side=RIGHT, padx=3)
        L4.pack(side=RIGHT, padx=3)
        L3.pack(side=RIGHT, padx=3)
        L2.pack(side=RIGHT, padx=3)
        L1.pack(side=RIGHT, padx=3)

        L1 = Label(mframe, font=("Apple, 10"))
        L1.pack()
        # End of wrodle UI....

        self.username = StringVar()
        self.password = StringVar()
        self.tmpemail = StringVar()

        Label(register_screen, text="Please enter details below", bg="blue",
              fg="white", width="300", height="2", font=("Calibri", 13)).pack()
        Label(register_screen, text="").pack()
        username_lable = Label(register_screen, text="Username * ")
        username_lable.pack()

        self.username_entry = Entry(register_screen, textvariable=self.username)
        self.username_entry.pack()
        
        password_lable = Label(register_screen, text="Password * ")
        password_lable.pack()
        
        self.password_entry = Entry(register_screen, textvariable=self.password, show='*')
        self.password_entry.pack()
        
        email_lable = Label(register_screen, text="Email * ")
        email_lable.pack()
        
        self.email_entry = Entry(register_screen, textvariable=self.tmpemail)
        self.email_entry.pack()
        Label(register_screen, text="").pack()

        # This line is to add style to button texts.
        buttonFont = font.Font(size=12, weight='bold')
        Button(register_screen, text="Register", font="buttonFont", width=10,
               height=1, bg="blue", fg="magenta", command=lambda: self.register_user()).pack()


#This class is for the Login Page.
class LoginClass(mysqlCon):
    # Designing window for login.
    def login(self):
        global login_screen
        login_screen = Toplevel(main_screen)
        login_screen.title("Login")
        login_screen.geometry("350x500")

        # Added for Wordle....
        iframe = Frame(login_screen)
        iframe.pack()

        topframe = Frame(login_screen)
        topframe.pack()

        mframe = Frame(login_screen)
        mframe.pack()

        L1 = Label(iframe, font=("Apple, 10"))
        L1.pack()

        L1 = Label(topframe, text="W", font=("Apple, 25"), bg="#8FDE21", width=2)
        L2 = Label(topframe, text="O", font=("Apple, 25"), bg="#8FDE21", width=2)
        L3 = Label(topframe, text="R", font=("Apple, 25"), bg="#8FDE21", width=2)
        L4 = Label(topframe, text="D", font=("Apple, 25"), bg="#8FDE21", width=2)
        L5 = Label(topframe, text="L", font=("Apple, 25"), bg="#8FDE21", width=2)
        L6 = Label(topframe, text="E", font=("Apple, 25"), bg="#8FDE21", width=2)
        L6.pack(side=RIGHT, padx=3, pady=10)
        L5.pack(side=RIGHT, padx=3)
        L4.pack(side=RIGHT, padx=3)
        L3.pack(side=RIGHT, padx=3)
        L2.pack(side=RIGHT, padx=3)
        L1.pack(side=RIGHT, padx=3)

        L1 = Label(mframe, font=("Apple, 10"))
        L1.pack()
        # End of wrodle UI....

        Label(login_screen, text="Please enter details below to login", bg="blue",
              fg="white", width="300", height="2", font=("Calibri", 13)).pack()
        Label(login_screen, text="").pack()

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        Label(login_screen, text="Username * ").pack()
        self.username_login_entry = Entry(login_screen, textvariable=self.username_verify)
        self.username_login_entry.pack()

        Label(login_screen, text="").pack()
        Label(login_screen, text="Password * ").pack()
        self.password_login_entry = Entry(
            login_screen, textvariable=self.password_verify, show='*')
        self.password_login_entry.pack()
        Label(login_screen, text="").pack()

        # This line is to add style to button texts.
        buttonFont = font.Font(size=12, weight='bold')
        Button(login_screen, font="buttonFont", text="Login", bg="blue",
               fg="magenta", width=10, height=1, command=lambda: self.login_verify()).pack()


    # Implementing event on login button
    def login_verify(self):
        self.username = self.username_verify.get()
        self.password = self.password_verify.get()
        
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

        self.fndbconn()
        # checking here if the details are matching with mysqlconntable
        self.checkUser = self.fnLogin(self.username, self.password)
        
        print(self.checkUser)
        if (len(self.checkUser) > 0):
            Label(login_screen, text="Login Success",
                  fg="green", font=("calibri", 11)).pack()
            login_screen.destroy()
            # Calling Wordle Game Main UI.
            self.login_sucess()
        else:
            self.password_not_recognised()

    # Designing popup for login success
    def login_sucess(self):
        tmp = "Login Successfully!\nWelcome '" + self.username + "'!"
        messagebox.showinfo("Success!", tmp)
        main_screen.destroy()
        GameMainClass.wordle_test(self)

    # Designing popup for login invalid password
    def login_fail(self):
        messagebox.showinfo("Fail!", "Unauthorizes Access. Try Again!")


class UserAttemptClass(WordleClass):
    def fnCheckAttemptNo(self):
        # Using global variables to access in this function.
        global tmpLabel
        global tempCount
        global wordle_screen
        global nextlevelframe
        global tmpLabel
        # End

        # Checking attempt and then to check the user answer with final answer.
        print(f"Attempt# = {tempCount}")
        # --- For First attempt ----
        if tempCount == 1:
            row1e1_info = row1e1_entry.get()
            row1e2_info = row1e2_entry.get()
            row1e3_info = row1e3_entry.get()
            row1e4_info = row1e4_entry.get()
            row1e5_info = row1e5_entry.get()

            row1e1_entry.config(state="disabled")
            row1e2_entry.config(state="disabled")
            row1e3_entry.config(state="disabled")
            row1e4_entry.config(state="disabled")
            row1e5_entry.config(state="disabled")

            tmpAnswer = row1e1_info + row1e2_info + row1e3_info + row1e4_info + row1e5_info
            print(f"User's answer = {tmpAnswer}")
            greenList, yellowList, greyList = self.fnStoreUserInputList(
                tmpAnswer)
            print(greenList)
            print(yellowList)
            print(greyList)
            # If we write loop like this, i becomes value rather than position.
            for i in greenList:
                if i == 1:
                    row1e1_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 2:
                    row1e2_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 3:
                    row1e3_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 4:
                    row1e4_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 5:
                    row1e5_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
            for i in yellowList:
                if i == 1:
                    row1e1_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 2:
                    row1e2_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 3:
                    row1e3_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 4:
                    row1e4_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 5:
                    row1e5_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
            for i in greyList:
                if i == 1:
                    row1e1_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 2:
                    row1e2_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 3:
                    row1e3_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 4:
                    row1e4_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 5:
                    row1e5_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
            # Checking if answer is correct or not.
            if len(greenList) == 5:
                submitButton.destroy()
                tmpLabelcorrect = Label(
                    wordle_screen, text="Congratulations! Your Answer is CORRECT.", fg="green", font=("calibri", 11))
                tmpLabelcorrect.pack()

                # Answer submission button...
                # This line is to add style to button texts.
                buttonFont = font.Font(size=12, weight='bold')
                btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont",
                                      width=10, height=1, bg="dark green", fg="magenta")
                btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
                btnNextLevel.pack()
                btnNextLevel.config(command=self.fnNextLevel)
            else:
                tmpLabel = Label(
                    wordle_screen, text="Incorrect Answer. Try Again.", fg="green", font=("calibri", 11))
                tmpLabel.pack()
                tempCount += 1

        # --- For second attempt ----
        elif tempCount == 2:
            row2e1_info = row2e1_entry.get()
            row2e2_info = row2e2_entry.get()
            row2e3_info = row2e3_entry.get()
            row2e4_info = row2e4_entry.get()
            row2e5_info = row2e5_entry.get()

            row2e1_entry.config(state="disabled")
            row2e2_entry.config(state="disabled")
            row2e3_entry.config(state="disabled")
            row2e4_entry.config(state="disabled")
            row2e5_entry.config(state="disabled")

            tmpAnswer = row2e1_info + row2e2_info + row2e3_info + row2e4_info + row2e5_info
            print(f"User's answer = {tmpAnswer}")
            greenList, yellowList, greyList = self.fnStoreUserInputList(
                tmpAnswer)
            print(greenList)
            print(yellowList)
            print(greyList)
            for i in greenList:
                if i == 1:
                    row2e1_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 2:
                    row2e2_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 3:
                    row2e3_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 4:
                    row2e4_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 5:
                    row2e5_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
            for i in yellowList:
                if i == 1:
                    row2e1_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 2:
                    row2e2_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 3:
                    row2e3_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 4:
                    row2e4_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 5:
                    row2e5_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
            for i in greyList:
                if i == 1:
                    row2e1_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 2:
                    row2e2_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 3:
                    row2e3_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 4:
                    row2e4_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 5:
                    row2e5_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
            # Checking if answer is correct or not.
            tmpLabel.destroy()
            if len(greenList) == 5:
                submitButton.destroy()
                tmpLabelcorrect = Label(
                    wordle_screen, text="Congratulations! Your Answer is CORRECT.", fg="green", font=("calibri", 11))
                tmpLabelcorrect.pack()

                # Answer submission button...
                # This line is to add style to button texts.
                buttonFont = font.Font(size=12, weight='bold')
                btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont",
                                      width=10, height=1, bg="dark green", fg="magenta")
                btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
                btnNextLevel.pack()
                btnNextLevel.config(command=self.fnNextLevel)
            else:
                tmpLabel.destroy()
                tmpLabel = Label(
                    wordle_screen, text="Incorrect Answer. Try Again.", fg="green", font=("calibri", 11))
                tmpLabel.pack()
                tempCount += 1

        # ----- For third attempt ------
        elif tempCount == 3:
            row3e1_info = row3e1_entry.get()
            row3e2_info = row3e2_entry.get()
            row3e3_info = row3e3_entry.get()
            row3e4_info = row3e4_entry.get()
            row3e5_info = row3e5_entry.get()

            row3e1_entry.config(state="disabled")
            row3e2_entry.config(state="disabled")
            row3e3_entry.config(state="disabled")
            row3e4_entry.config(state="disabled")
            row3e5_entry.config(state="disabled")

            tmpAnswer = row3e1_info + row3e2_info + row3e3_info + row3e4_info + row3e5_info
            print(f"User's answer = {tmpAnswer}")
            greenList, yellowList, greyList = self.fnStoreUserInputList(
                tmpAnswer)
            print(greenList)
            print(yellowList)
            print(greyList)
            for i in greenList:
                if i == 1:
                    row3e1_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 2:
                    row3e2_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 3:
                    row3e3_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 4:
                    row3e4_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 5:
                    row3e5_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
            for i in yellowList:
                if i == 1:
                    row3e1_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 2:
                    row3e2_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 3:
                    row3e3_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 4:
                    row3e4_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 5:
                    row3e5_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
            for i in greyList:
                if i == 1:
                    row3e1_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 2:
                    row3e2_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 3:
                    row3e3_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 4:
                    row3e4_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 5:
                    row3e5_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
            # Checking if answer is correct or not.
            tmpLabel.destroy()
            if len(greenList) == 5:
                submitButton.destroy()
                tmpLabelcorrect = Label(
                    wordle_screen, text="Congratulations! Your Answer is CORRECT.", fg="green", font=("calibri", 11))
                tmpLabelcorrect.pack()

                # Answer submission button...
                # This line is to add style to button texts.
                buttonFont = font.Font(size=12, weight='bold')
                btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont",
                                      width=10, height=1, bg="dark green", fg="magenta")
                btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
                btnNextLevel.pack()
                btnNextLevel.config(command=self.fnNextLevel)
            else:
                tmpLabel.destroy()
                tmpLabel = Label(
                    wordle_screen, text="Incorrect Answer. Try Again.", fg="green", font=("calibri", 11))
                tmpLabel.pack()
                tempCount += 1

        # Checking for FORTH attempt ----.
        elif tempCount == 4:
            row4e1_info = row4e1_entry.get()
            row4e2_info = row4e2_entry.get()
            row4e3_info = row4e3_entry.get()
            row4e4_info = row4e4_entry.get()
            row4e5_info = row4e5_entry.get()

            row4e1_entry.config(state="disabled")
            row4e2_entry.config(state="disabled")
            row4e3_entry.config(state="disabled")
            row4e4_entry.config(state="disabled")
            row4e5_entry.config(state="disabled")

            tmpAnswer = row4e1_info + row4e2_info + row4e3_info + row4e4_info + row4e5_info
            print(f"User's answer = {tmpAnswer}")
            greenList, yellowList, greyList = self.fnStoreUserInputList(
                tmpAnswer)
            print(greenList)
            print(yellowList)
            print(greyList)
            for i in greenList:
                if i == 1:
                    row4e1_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 2:
                    row4e2_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 3:
                    row4e3_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 4:
                    row4e4_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 5:
                    row4e5_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
            for i in yellowList:
                if i == 1:
                    row4e1_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 2:
                    row4e2_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 3:
                    row4e3_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 4:
                    row4e4_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 5:
                    row4e5_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
            for i in greyList:
                if i == 1:
                    row4e1_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 2:
                    row4e2_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 3:
                    row4e3_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 4:
                    row4e4_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 5:
                    row4e5_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
            # Checking if answer is correct or not.
            tmpLabel.destroy()
            if len(greenList) == 5:
                submitButton.destroy()
                tmpLabelcorrect = Label(
                    wordle_screen, text="Congratulations! Your Answer is CORRECT.", fg="green", font=("calibri", 11))
                tmpLabelcorrect.pack()

                # Answer submission button...
                # This line is to add style to button texts.
                buttonFont = font.Font(size=12, weight='bold')
                btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont",
                                      width=10, height=1, bg="dark green", fg="magenta")
                btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
                btnNextLevel.pack()
                btnNextLevel.config(command=self.fnNextLevel)
            else:
                tmpLabel.destroy()
                tmpLabel = Label(
                    wordle_screen, text="Incorrect Answer. Try Again.", fg="green", font=("calibri", 11))
                tmpLabel.pack()
                tempCount += 1

        # Checking for FIFTH attempt ----.
        elif tempCount == 5:
            row5e1_info = row5e1_entry.get()
            row5e2_info = row5e2_entry.get()
            row5e3_info = row5e3_entry.get()
            row5e4_info = row5e4_entry.get()
            row5e5_info = row5e5_entry.get()

            row5e1_entry.config(state="disabled")
            row5e2_entry.config(state="disabled")
            row5e3_entry.config(state="disabled")
            row5e4_entry.config(state="disabled")
            row5e5_entry.config(state="disabled")

            tmpAnswer = row5e1_info + row5e2_info + row5e3_info + row5e4_info + row5e5_info
            print(f"User's answer = {tmpAnswer}")
            greenList, yellowList, greyList = self.fnStoreUserInputList(
                tmpAnswer)
            print(greenList)
            print(yellowList)
            print(greyList)
            for i in greenList:
                if i == 1:
                    row5e1_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 2:
                    row5e2_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 3:
                    row5e3_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 4:
                    row5e4_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 5:
                    row5e5_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
            for i in yellowList:
                if i == 1:
                    row5e1_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 2:
                    row5e2_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 3:
                    row5e3_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 4:
                    row5e4_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 5:
                    row5e5_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
            for i in greyList:
                if i == 1:
                    row5e1_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 2:
                    row5e2_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 3:
                    row5e3_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 4:
                    row5e4_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 5:
                    row5e5_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
            # Checking if answer is correct or not.
            tmpLabel.destroy()
            if len(greenList) == 5:
                submitButton.destroy()
                tmpLabelcorrect = Label(
                    wordle_screen, text="Congratulations! Your Answer is CORRECT.", fg="green", font=("calibri", 11))
                tmpLabelcorrect.pack()

                # Answer submission button...
                # This line is to add style to button texts.
                buttonFont = font.Font(size=12, weight='bold')
                btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont",
                                      width=10, height=1, bg="dark green", fg="magenta")
                btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
                btnNextLevel.pack()
                btnNextLevel.config(command=self.fnNextLevel)
            else:
                tmpLabel.destroy()
                tmpLabel = Label(
                    wordle_screen, text="Incorrect Answer. Try Again.", fg="green", font=("calibri", 11))
                tmpLabel.pack()
                tempCount += 1

        # Checking for SIXTH attempt ----.
        elif tempCount == 6:
            row6e1_info = row6e1_entry.get()
            row6e2_info = row6e2_entry.get()
            row6e3_info = row6e3_entry.get()
            row6e4_info = row6e4_entry.get()
            row6e5_info = row6e5_entry.get()

            row6e1_entry.config(state="disabled")
            row6e2_entry.config(state="disabled")
            row6e3_entry.config(state="disabled")
            row6e4_entry.config(state="disabled")
            row6e5_entry.config(state="disabled")

            tmpAnswer = row6e1_info + row6e2_info + row6e3_info + row6e4_info + row6e5_info
            print(f"User's answer = {tmpAnswer}")
            greenList, yellowList, greyList = self.fnStoreUserInputList(
                tmpAnswer)
            print(greenList)
            print(yellowList)
            print(greyList)
            for i in greenList:
                if i == 1:
                    row6e1_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 2:
                    row6e2_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 3:
                    row6e3_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 4:
                    row6e4_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
                if i == 5:
                    row6e5_entry.configure(
                        disabledbackground="green", state="disabled", disabledforeground="black")
            for i in yellowList:
                if i == 1:
                    row6e1_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 2:
                    row6e2_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 3:
                    row6e3_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 4:
                    row6e4_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
                if i == 5:
                    row6e5_entry.configure(
                        disabledbackground="yellow", state="disabled", disabledforeground="black")
            for i in greyList:
                if i == 1:
                    row6e1_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 2:
                    row6e2_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 3:
                    row6e3_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 4:
                    row6e4_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
                if i == 5:
                    row6e5_entry.configure(
                        disabledbackground="grey", state="disabled", disabledforeground="black")
            # Checking if answer is correct or not.
            tmpLabel.destroy()
            if len(greenList) == 5:
                submitButton.destroy()
                tmpLabelcorrect = Label(
                    wordle_screen, text="Congratulations! Your Answer is CORRECT.", fg="green", font=("calibri", 11))
                tmpLabelcorrect.pack()

                # Answer submission button...
                # This line is to add style to button texts.
                buttonFont = font.Font(size=12, weight='bold')
                btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont",
                                      width=10, height=1, bg="dark green", fg="magenta")
                btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
                btnNextLevel.pack()
                btnNextLevel.config(command=self.fnNextLevel)
            else:
                # Destroying previous label(because I can't print label six times. So destroying previous label and then overriding next label.)
                submitButton.destroy()
                tmpLabel.destroy()
                tmpLabel = Label(
                    wordle_screen, text="Incorrect Answer. You lose this game. No Attempts Remain.", fg="green", font=("calibri", 11))
                tmpLabel.pack()

                # Calling function to get correct answer.
                self.finalWord = self.getCorrectAnswer()

                # Printing correct answer.
                Label(wordle_screen, text="Correct Answer Is...",
                      fg="blue", font=("calibri", 15)).pack()
                Label(wordle_screen, text=self.finalWord,
                      fg="blue", font=("calibri", 15)).pack()

                # Answer submission button...
                # This line is to add style to button texts.
                buttonFont = font.Font(size=12, weight='bold')
                btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont",
                                      width=10, height=1, bg="dark green", fg="magenta")
                btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
                btnNextLevel.pack()
                btnNextLevel.config(command=self.fnNextLevel)
                tempCount = 1


    def fnNextLevel(self):
        global wordle_screen
        wordle_screen.destroy()
        self.wordle_test()

class GameMainClass(RegisterClass, LoginClass, UserAttemptClass, WordleClass):
    # Designing Main(first) window
    def main_account_screen(self):
        global main_screen
        main_screen = Tk()
        main_screen.geometry("350x500")
        main_screen.title("Account Login")

        # Added for Wordle....
        iframe = Frame(main_screen)
        iframe.pack()

        topframe = Frame(main_screen)
        topframe.pack()

        mframe = Frame(main_screen)
        mframe.pack()

        L1 = Label(iframe, font=("Apple, 10"))
        L1.pack()

        L1 = Label(topframe, text="W", font=("Apple, 25"), bg="#8FDE21", width=2)
        L2 = Label(topframe, text="O", font=("Apple, 25"), bg="#8FDE21", width=2)
        L3 = Label(topframe, text="R", font=("Apple, 25"), bg="#8FDE21", width=2)
        L4 = Label(topframe, text="D", font=("Apple, 25"), bg="#8FDE21", width=2)
        L5 = Label(topframe, text="L", font=("Apple, 25"), bg="#8FDE21", width=2)
        L6 = Label(topframe, text="E", font=("Apple, 25"), bg="#8FDE21", width=2)
        L6.pack(side=RIGHT, padx=3, pady=10)
        L5.pack(side=RIGHT, padx=3)
        L4.pack(side=RIGHT, padx=3)
        L3.pack(side=RIGHT, padx=3)
        L2.pack(side=RIGHT, padx=3)
        L1.pack(side=RIGHT, padx=3)

        L1 = Label(mframe, font=("Apple, 10"))
        L1.pack()
        # End of wrodle UI....

        Label(text="Select Your Choice", bg="blue", fg="white",
              width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()

        # This line is to add style to button texts.
        buttonFont = font.Font(size=12, weight='bold')

        Button(text="Login", font="buttonFont", height="2",
               width="20", bg="blue", fg="magenta", command=lambda:self.login()).pack()
        Label(text="").pack()
        button = Button(text="Register", font="buttonFont", height="2",
                        width="20", bg="blue", fg="magenta", command=lambda: self.register()).pack()
        main_screen.mainloop()


    # Starting wordle GAME UI--------
    # ----- Main wordle game UI for every attemts ------.
    def wordle_test(self):

        global nextlevelframe  # This frame to give next button.
        global tempCount
        tempCount = 1

        from tkinter import LEFT, RIGHT, Button, Entry, Frame, Label, StringVar, Tk, Toplevel, font
        global submitButton
        global wordle_screen

        wordle_screen = Tk()
        wordle_screen.title("Wordle Game Main Screen")
        wordle_screen.geometry("400x650")
        # ---Frames are added ---.
        topframe = Frame(wordle_screen)
        topframe.pack()
        mframe = Frame(wordle_screen)
        mframe.pack()
        iframe = Frame(wordle_screen)
        iframe.pack()
        hintframe = Frame(wordle_screen)
        hintframe.pack()
        frame1 = Frame(wordle_screen)
        frame1.pack()
        frame2 = Frame(wordle_screen)
        frame2.pack()
        frame3 = Frame(wordle_screen)
        frame3.pack()
        frame4 = Frame(wordle_screen)
        frame4.pack()
        frame5 = Frame(wordle_screen)
        frame5.pack()
        frame6 = Frame(wordle_screen)
        frame6.pack()
        bottomframe = Frame(wordle_screen)
        bottomframe.pack()
        nextlevelframe = Frame(wordle_screen)
        nextlevelframe.pack()

        L1 = Label(topframe, font=("Apple, 20"), text="")
        L1.pack()

        L1 = Label(mframe, text="W", font=("Apple, 25"), bg="#8FDE21", width=2)
        L2 = Label(mframe, text="O", font=("Apple, 25"), bg="#8FDE21", width=2)
        L3 = Label(mframe, text="R", font=("Apple, 25"), bg="#8FDE21", width=2)
        L4 = Label(mframe, text="D", font=("Apple, 25"), bg="#8FDE21", width=2)
        L5 = Label(mframe, text="L", font=("Apple, 25"), bg="#8FDE21", width=2)
        L6 = Label(mframe, text="E", font=("Apple, 25"), bg="#8FDE21", width=2)
        L6.pack(side=RIGHT, padx=3, pady=20)
        L5.pack(side=RIGHT, padx=3)
        L4.pack(side=RIGHT, padx=3)
        L3.pack(side=RIGHT, padx=3)
        L2.pack(side=RIGHT, padx=3)
        L1.pack(side=RIGHT, padx=3)

        # Printing username in top right corner.
        tmpUserPrint = "Welcome " + '"' + self.username + '"'
        L7 = Label(wordle_screen, text=tmpUserPrint,
                   fg="#101057", font=("Calibri", 16))
        L7.place(relx=1.0, rely=0.0, anchor='ne')

        Label(iframe, text="Please enter details below", bg="blue",
              fg="white", width="300", height="1", font=("Calibri", 13)).pack()
        Label(iframe, text="").pack(pady=4)

        # Logout button to configure.

        def fnLogout():
            global wordle_screen
            wordle_screen.destroy()

        logoutButton = Button(wordle_screen, font="buttonFont", text="Logout",
                              fg="magenta", bg="#f7051d", borderwidth=2, relief="solid", command=fnLogout)
        logoutButton.place(relx=0.05, rely=0.97, anchor='sw')
        # End of Logout button code.

        # Calling this function to get New Final Word for this level.
        self.finalWord = self.getNewFinalWord()
        hint = self.finalWord[0]
        finalhint = "Today's word start from " + '"' + hint + '"'

        self.hintLabel = Label(wordle_screen, text="Hint", width=6,
                          fg="magenta", bg="white", height="1", font=("Calibri", 13))
        self.hintLabel.place(rely=0.97, relx=0.97, x=0, y=0, anchor=SE)

        self.hintDisplayLabel = Label(wordle_screen)
        self.hintDisplayLabel.place(rely=0.97, relx=0.80, x=0, y=0, anchor=SE)

        def on_enter(event):
            self.hintDisplayLabel.configure(
                text=finalhint, fg="magenta", bg="white", height="1", font=("Calibri", 13))

        def on_leave(enter):
            self.hintDisplayLabel.configure(text="", bg="#fafaf2")

        # We can bind the key event using the Binding method in a tkinter application.
        self.hintLabel.bind("<Enter>", on_enter)
        self.hintLabel.bind("<Leave>", on_leave)
        # Whenever the key will be triggered, it will call a handler that will raise the specific operation for the key event.
        # End of the hint code.


        # --- Starting Wordle Game UI for FIRST row. ---.
        global row1e1
        global row1e2
        global row1e3
        global row1e4
        global row1e5

        global row1e1_entry
        global row1e2_entry
        global row1e3_entry
        global row1e4_entry
        global row1e5_entry

        row1e1 = StringVar()
        row1e2 = StringVar()
        row1e3 = StringVar()
        row1e4 = StringVar()
        row1e5 = StringVar()

        row1e1_entry = Entry(frame1, textvariable=row1e1, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row1e1_entry.pack(side=LEFT, padx=5, pady=5)
        row1e2_entry = Entry(frame1, textvariable=row1e2, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row1e2_entry.pack(side=LEFT, padx=5, pady=5)
        row1e3_entry = Entry(frame1, textvariable=row1e3, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row1e3_entry.pack(side=LEFT, padx=5, pady=5)
        row1e4_entry = Entry(frame1, textvariable=row1e4, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row1e4_entry.pack(side=LEFT, padx=5, pady=5)
        row1e5_entry = Entry(frame1, textvariable=row1e5, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row1e5_entry.pack(side=LEFT)

        # --- Starting Wordle Game UI for SECOND row. ---.
        global row2e1
        global row2e2
        global row2e3
        global row2e4
        global row2e5

        global row2e1_entry
        global row2e2_entry
        global row2e3_entry
        global row2e4_entry
        global row2e5_entry

        row2e1 = StringVar()
        row2e2 = StringVar()
        row2e3 = StringVar()
        row2e4 = StringVar()
        row2e5 = StringVar()

        row2e1_entry = Entry(frame2, textvariable=row2e1, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row2e1_entry.pack(side=LEFT, padx=5, pady=5)
        row2e2_entry = Entry(frame2, textvariable=row2e2, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row2e2_entry.pack(side=LEFT, padx=5, pady=5)
        row2e3_entry = Entry(frame2, textvariable=row2e3, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row2e3_entry.pack(side=LEFT, padx=5, pady=5)
        row2e4_entry = Entry(frame2, textvariable=row2e4, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row2e4_entry.pack(side=LEFT, padx=5, pady=5)
        row2e5_entry = Entry(frame2, textvariable=row2e5, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row2e5_entry.pack(side=LEFT)

        # --- Starting Wordle Game UI for THIRD row. ---.
        global row3e1
        global row3e2
        global row3e3
        global row3e4
        global row3e5

        global row3e1_entry
        global row3e2_entry
        global row3e3_entry
        global row3e4_entry
        global row3e5_entry

        row3e1 = StringVar()
        row3e2 = StringVar()
        row3e3 = StringVar()
        row3e4 = StringVar()
        row3e5 = StringVar()

        row3e1_entry = Entry(frame3, textvariable=row3e1, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row3e1_entry.pack(side=LEFT, padx=5, pady=5)
        row3e2_entry = Entry(frame3, textvariable=row3e2, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row3e2_entry.pack(side=LEFT, padx=5, pady=5)
        row3e3_entry = Entry(frame3, textvariable=row3e3, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row3e3_entry.pack(side=LEFT, padx=5, pady=5)
        row3e4_entry = Entry(frame3, textvariable=row3e4, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row3e4_entry.pack(side=LEFT, padx=5, pady=5)
        row3e5_entry = Entry(frame3, textvariable=row3e5, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row3e5_entry.pack(side=LEFT)

        # --- Starting Wordle Game UI for FORTH row. ---.
        global row4e1
        global row4e2
        global row4e3
        global row4e4
        global row4e5

        global row4e1_entry
        global row4e2_entry
        global row4e3_entry
        global row4e4_entry
        global row4e5_entry

        row4e1 = StringVar()
        row4e2 = StringVar()
        row4e3 = StringVar()
        row4e4 = StringVar()
        row4e5 = StringVar()

        row4e1_entry = Entry(frame4, textvariable=row4e1, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row4e1_entry.pack(side=LEFT, padx=5, pady=5)
        row4e2_entry = Entry(frame4, textvariable=row4e2, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row4e2_entry.pack(side=LEFT, padx=5, pady=5)
        row4e3_entry = Entry(frame4, textvariable=row4e3, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row4e3_entry.pack(side=LEFT, padx=5, pady=5)
        row4e4_entry = Entry(frame4, textvariable=row4e4, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row4e4_entry.pack(side=LEFT, padx=5, pady=5)
        row4e5_entry = Entry(frame4, textvariable=row4e5, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row4e5_entry.pack(side=LEFT)

        # --- Starting Wordle Game UI for FIFTH row. ---.
        global row5e1
        global row5e2
        global row5e3
        global row5e4
        global row5e5

        global row5e1_entry
        global row5e2_entry
        global row5e3_entry
        global row5e4_entry
        global row5e5_entry

        row5e1 = StringVar()
        row5e2 = StringVar()
        row5e3 = StringVar()
        row5e4 = StringVar()
        row5e5 = StringVar()

        row5e1_entry = Entry(frame5, textvariable=row5e1, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row5e1_entry.pack(side=LEFT, padx=5, pady=5)
        row5e2_entry = Entry(frame5, textvariable=row5e2, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row5e2_entry.pack(side=LEFT, padx=5, pady=5)
        row5e3_entry = Entry(frame5, textvariable=row5e3, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row5e3_entry.pack(side=LEFT, padx=5, pady=5)
        row5e4_entry = Entry(frame5, textvariable=row5e4, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row5e4_entry.pack(side=LEFT, padx=5, pady=5)
        row5e5_entry = Entry(frame5, textvariable=row5e5, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row5e5_entry.pack(side=LEFT)

        # --- Starting Wordle Game UI for SIXTH row. ---.
        global row6e1
        global row6e2
        global row6e3
        global row6e4
        global row6e5

        global row6e1_entry
        global row6e2_entry
        global row6e3_entry
        global row6e4_entry
        global row6e5_entry

        row6e1 = StringVar()
        row6e2 = StringVar()
        row6e3 = StringVar()
        row6e4 = StringVar()
        row6e5 = StringVar()

        row6e1_entry = Entry(frame6, textvariable=row6e1, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row6e1_entry.pack(side=LEFT, padx=5, pady=5)
        row6e2_entry = Entry(frame6, textvariable=row6e2, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row6e2_entry.pack(side=LEFT, padx=5, pady=5)
        row6e3_entry = Entry(frame6, textvariable=row6e3, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row6e3_entry.pack(side=LEFT, padx=5, pady=5)
        row6e4_entry = Entry(frame6, textvariable=row6e4, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row6e4_entry.pack(side=LEFT, padx=5, pady=5)
        row6e5_entry = Entry(frame6, textvariable=row6e5, width=2, font=(
            'Geogia 20'), bg='black', fg='white', justify='center')
        row6e5_entry.pack(side=LEFT)

        # Answer submission button...
        # This line is to add style to button texts.
        buttonFont = font.Font(size=12, weight='bold')
        submitButton = Button(bottomframe, text="Submit", font="buttonFont",
                              width=10, height=1, bg="blue", fg="magenta")
        submitButton.pack(pady=20)
        submitButton.config(command=self.fnCheckAttemptNo)
        wordle_screen.mainloop()

    # -------- Function to check which attempt this is ----

# Calling main account function. Beginning Page.8
tmpObj = GameMainClass()
tmpObj.main_account_screen()