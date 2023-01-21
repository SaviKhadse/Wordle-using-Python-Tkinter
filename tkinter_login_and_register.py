#import modules
 
from cgitb import text
from ctypes.wintypes import SIZE
from tkinter import *
import os
from tkinter import messagebox
from tkinter import font
from itertools import count
from tkinter import END, Label, messagebox
from turtle import width

#Importing wordle_program_class and using methods of that program.
from tkinter_wordle_game_main_loagical_program import WordleClass

global tempCount    #This variable to call word to check as per the attempts.
tempCount = 1

global username1
global nextlevelframe
global hintLabel
global hintDisplayLabel

#importing database class from file name called "tkinter_dbconeection_file.py"
from tkinter_dbconnection_file import mysqlCon
mysqlCon.fndbconn()

# Designing window for registration 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("350x500")

    #Added for Wordle....
    iframe = Frame(register_screen)
    iframe.pack()

    topframe = Frame(register_screen)
    topframe.pack()

    mframe = Frame(register_screen)
    mframe.pack()

    L1=Label(iframe, font=("Apple, 10"))
    L1.pack()

    L1=Label(topframe, text="W", font=("Apple, 25"), bg="#8FDE21", width=2)
    L2=Label(topframe, text="O", font=("Apple, 25"), bg="#8FDE21", width=2)
    L3=Label(topframe, text="R", font=("Apple, 25"), bg="#8FDE21", width=2)
    L4=Label(topframe, text="D", font=("Apple, 25"), bg="#8FDE21", width=2)
    L5=Label(topframe, text="L", font=("Apple, 25"), bg="#8FDE21", width=2)
    L6=Label(topframe, text="E", font=("Apple, 25"), bg="#8FDE21", width=2)
    L6.pack(side = RIGHT, padx=3, pady=10)
    L5.pack(side = RIGHT, padx=3)
    L4.pack(side = RIGHT, padx=3)
    L3.pack(side = RIGHT, padx=3)
    L2.pack(side = RIGHT, padx=3)
    L1.pack(side = RIGHT, padx=3)

    L1=Label(mframe, font=("Apple, 10"))
    L1.pack()
    #End of wrodle UI....
 
    global username
    global password
    global tmpemail
    global username_entry
    global password_entry
    global email_entry
    username = StringVar()
    password = StringVar()
    tmpemail = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue", fg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    email_lable = Label(register_screen, text="Email * ")
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=tmpemail)
    email_entry.pack()
    Label(register_screen, text="").pack()

    buttonFont = font.Font(size=12, weight='bold')  #This line is to add style to button texts.
    Button(register_screen, text="Register", font="buttonFont", width=10, height=1, bg="blue", fg="white", command = register_user).pack()

# Designing window for login.
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("350x500")

    #Added for Wordle....
    iframe = Frame(login_screen)
    iframe.pack()

    topframe = Frame(login_screen)
    topframe.pack()

    mframe = Frame(login_screen)
    mframe.pack()

    L1=Label(iframe, font=("Apple, 10"))
    L1.pack()

    L1=Label(topframe, text="W", font=("Apple, 25"), bg="#8FDE21", width=2)
    L2=Label(topframe, text="O", font=("Apple, 25"), bg="#8FDE21", width=2)
    L3=Label(topframe, text="R", font=("Apple, 25"), bg="#8FDE21", width=2)
    L4=Label(topframe, text="D", font=("Apple, 25"), bg="#8FDE21", width=2)
    L5=Label(topframe, text="L", font=("Apple, 25"), bg="#8FDE21", width=2)
    L6=Label(topframe, text="E", font=("Apple, 25"), bg="#8FDE21", width=2)
    L6.pack(side = RIGHT, padx=3, pady=10)
    L5.pack(side = RIGHT, padx=3)
    L4.pack(side = RIGHT, padx=3)
    L3.pack(side = RIGHT, padx=3)
    L2.pack(side = RIGHT, padx=3)
    L1.pack(side = RIGHT, padx=3)

    L1=Label(mframe, font=("Apple, 10"))
    L1.pack()
    #End of wrodle UI....

    Label(login_screen, text="Please enter details below to login", bg="blue", fg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()

    buttonFont = font.Font(size=12, weight='bold')  #This line is to add style to button texts.
    Button(login_screen, font="buttonFont", text="Login", bg="blue", fg="white", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
    email_info = tmpemail.get()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)

    checkUser=mysqlCon.fnRegister(username_info,password_info,email_info)

    messagebox.showinfo("Success!","Welcome! Registration Done Suceessfully..")
    register_screen.destroy()
 
# Implementing event on login button 
 
def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    mysqlCon.fndbconn()
    checkUser=mysqlCon.fnLogin(username1,password1)
    if len(checkUser)>0:
        Label(login_screen, text="Login Success", fg="green", font=("calibri", 11)).pack()
        login_screen.destroy()
        #Calling Wordle Game Main UI.
        login_sucess()
    else:
        password_not_recognised()
 
# Designing popup for login success
 
def login_sucess():
    #global Toplevel
    #global login_success_screen
    #login_success_screen = Toplevel(login_screen)
    #login_success_screen.title("Success")
    #login_success_screen.geometry("150x100")
    messagebox.showinfo("Suceess","Welcome to game!5")
    wordle_test()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 

# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("350x500")
    main_screen.title("Account Login")

    #Added for Wordle....
    iframe = Frame(main_screen)
    iframe.pack()

    topframe = Frame(main_screen)
    topframe.pack()

    mframe = Frame(main_screen)
    mframe.pack()

    L1=Label(iframe, font=("Apple, 10"))
    L1.pack()

    L1=Label(topframe, text="W", font=("Apple, 25"), bg="#8FDE21", width=2)
    L2=Label(topframe, text="O", font=("Apple, 25"), bg="#8FDE21", width=2)
    L3=Label(topframe, text="R", font=("Apple, 25"), bg="#8FDE21", width=2)
    L4=Label(topframe, text="D", font=("Apple, 25"), bg="#8FDE21", width=2)
    L5=Label(topframe, text="L", font=("Apple, 25"), bg="#8FDE21", width=2)
    L6=Label(topframe, text="E", font=("Apple, 25"), bg="#8FDE21", width=2)
    L6.pack(side = RIGHT, padx=3, pady=10)
    L5.pack(side = RIGHT, padx=3)
    L4.pack(side = RIGHT, padx=3)
    L3.pack(side = RIGHT, padx=3)
    L2.pack(side = RIGHT, padx=3)
    L1.pack(side = RIGHT, padx=3)

    L1=Label(mframe, font=("Apple, 10"))
    L1.pack()
    #End of wrodle UI....

    Label(text="Select Your Choice", bg="blue", fg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    buttonFont = font.Font(size=12, weight='bold')  #This line is to add style to button texts.

    Button(text="Login", font="buttonFont", height="2", width="20", bg="blue", fg="white", command = login).pack()
    Label(text="").pack()
    button = Button(text="Register", font="buttonFont", height="2", width="20", bg="blue", fg="white", command=register).pack()
    main_screen.mainloop()


#Starting wordle GAME UI--------

#----- Main wordle game UI for every attemts ------.
def wordle_test():

    global username1 #This variable is used to display UserName.
    global nextlevelframe #This frame to give next button.

    from tkinter import LEFT, RIGHT, Button, Entry, Frame, Label, StringVar, Tk, Toplevel, font
    global submitButton
    global wordle_screen
    wordle_screen = Tk()
    wordle_screen.title("Wordle Game Main Screen")
    wordle_screen.geometry("400x650")
    #---Frames are added ---.
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

    L1=Label(topframe, font=("Apple, 20"), text="")
    L1.pack()

    L1=Label(mframe, text="W", font=("Apple, 25"), bg="#8FDE21", width=2)
    L2=Label(mframe, text="O", font=("Apple, 25"), bg="#8FDE21", width=2)
    L3=Label(mframe, text="R", font=("Apple, 25"), bg="#8FDE21", width=2)
    L4=Label(mframe, text="D", font=("Apple, 25"), bg="#8FDE21", width=2)
    L5=Label(mframe, text="L", font=("Apple, 25"), bg="#8FDE21", width=2)
    L6=Label(mframe, text="E", font=("Apple, 25"), bg="#8FDE21", width=2)
    L6.pack(side = RIGHT, padx=3, pady=20)
    L5.pack(side = RIGHT, padx=3)
    L4.pack(side = RIGHT, padx=3)
    L3.pack(side = RIGHT, padx=3)
    L2.pack(side = RIGHT, padx=3)
    L1.pack(side = RIGHT, padx=3)

    #Printing username in top right corner.
    tmpUserPrint = "Welcome " + '"' + username1 + '"'
    L7 = Label(wordle_screen, text=tmpUserPrint, fg="#101057", font=("Calibri", 16))
    L7.place(relx=1.0, rely=0.0, anchor='ne')       

    Label(iframe, text="Please enter details below", bg="blue", fg="white", width="300", height="1", font=("Calibri", 13)).pack()
    Label(iframe, text="").pack(pady=4)


    #Logout button to configure.
    def fnLogout():
        global wordle_screen
        wordle_screen.destroy()

    logoutButton = Button(wordle_screen, font="buttonFont",text="Logout", fg="white", bg="#f7051d", borderwidth=1,command=fnLogout)
    logoutButton.place(relx=0.05, rely=0.97, anchor='sw')
    #End of Logout button code.


    #Hint to setup
    global hintLabel
    global hintDisplayLabel

    #Calling this function to get New Final Word for this level.
    finalWord = WordleClass.getNewFinalWord()
    hint = finalWord[0]
    finalhint = "Today's word start from " + '"' + hint + '"'

    hintLabel = Label(wordle_screen, text="Hint", width=6, fg="white", bg="#04c91f", height="1", font=("Calibri", 13))
    hintLabel.place(relx=0.98, rely=0.24, anchor='ne')

    hintDisplayLabel = Label(wordle_screen)
    hintDisplayLabel.place(relx=0.76, rely=0.23, anchor='ne')

    def on_enter(event):
        global hintDisplayLabel
        hintDisplayLabel.configure(text=finalhint, fg="white", bg="#04c91f", height="1", font=("Calibri", 13))

    def on_leave(enter):
        global hintDisplayLabel
        hintDisplayLabel.configure(text="", bg="#fafaf2")

    hintLabel.bind("<Enter>", on_enter)
    hintLabel.bind("<Leave>", on_leave)
    #End of the hint code.  

    #--- Starting Wordle Game UI for FIRST row. ---.
    global row1e1
    global row1e2
    global row1e3
    global row1e4
    global row1e1_entry
    global row1e2_entry
    global row1e3_entry
    global row1e4_entry
    row1e1 = StringVar()
    row1e2 = StringVar()
    row1e3 = StringVar()
    row1e4 = StringVar()
    row1e1_entry = Entry(frame1, textvariable=row1e1, width = 2,font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row1e1_entry.pack(side = LEFT, padx=5, pady=5)
    row1e2_entry = Entry(frame1, textvariable=row1e2, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row1e2_entry.pack(side = LEFT, padx=5, pady=5)
    row1e3_entry = Entry(frame1, textvariable=row1e3, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row1e3_entry.pack(side = LEFT, padx=5, pady=5)
    row1e4_entry = Entry(frame1, textvariable=row1e4, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row1e4_entry.pack(side = LEFT)
    #--- Starting Wordle Game UI for SECOND row. ---.
    global row2e1
    global row2e2
    global row2e3
    global row2e4
    global row2e1_entry
    global row2e2_entry
    global row2e3_entry
    global row2e4_entry
    row2e1 = StringVar()
    row2e2 = StringVar()
    row2e3 = StringVar()
    row2e4 = StringVar()
    row2e1_entry = Entry(frame2, textvariable=row2e1, width = 2,font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row2e1_entry.pack(side = LEFT, padx=5, pady=5)
    row2e2_entry = Entry(frame2, textvariable=row2e2, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row2e2_entry.pack(side = LEFT, padx=5, pady=5)
    row2e3_entry = Entry(frame2, textvariable=row2e3, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row2e3_entry.pack(side = LEFT, padx=5, pady=5)
    row2e4_entry = Entry(frame2, textvariable=row2e4, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row2e4_entry.pack(side = LEFT)
    #--- Starting Wordle Game UI for THIRD row. ---.
    global row3e1
    global row3e2
    global row3e3
    global row3e4
    global row3e1_entry
    global row3e2_entry
    global row3e3_entry
    global row3e4_entry
    row3e1 = StringVar()
    row3e2 = StringVar()
    row3e3 = StringVar()
    row3e4 = StringVar()
    row3e1_entry = Entry(frame3, textvariable=row3e1, width = 2,font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row3e1_entry.pack(side = LEFT, padx=5, pady=5)
    row3e2_entry = Entry(frame3, textvariable=row3e2, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row3e2_entry.pack(side = LEFT, padx=5, pady=5)
    row3e3_entry = Entry(frame3, textvariable=row3e3, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row3e3_entry.pack(side = LEFT, padx=5, pady=5)
    row3e4_entry = Entry(frame3, textvariable=row3e4, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row3e4_entry.pack(side = LEFT)
    #--- Starting Wordle Game UI for FORTH row. ---.
    global row4e1
    global row4e2
    global row4e3
    global row4e4
    global row4e1_entry
    global row4e2_entry
    global row4e3_entry
    global row4e4_entry
    row4e1 = StringVar()
    row4e2 = StringVar()
    row4e3 = StringVar()
    row4e4 = StringVar()
    row4e1_entry = Entry(frame4, textvariable=row4e1, width = 2,font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row4e1_entry.pack(side = LEFT, padx=5, pady=5)
    row4e2_entry = Entry(frame4, textvariable=row4e2, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row4e2_entry.pack(side = LEFT, padx=5, pady=5)
    row4e3_entry = Entry(frame4, textvariable=row4e3, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row4e3_entry.pack(side = LEFT, padx=5, pady=5)
    row4e4_entry = Entry(frame4, textvariable=row4e4, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row4e4_entry.pack(side = LEFT)
    #--- Starting Wordle Game UI for FIFTH row. ---.
    global row5e1
    global row5e2
    global row5e3
    global row5e4
    global row5e1_entry
    global row5e2_entry
    global row5e3_entry
    global row5e4_entry
    row5e1 = StringVar()
    row5e2 = StringVar()
    row5e3 = StringVar()
    row5e4 = StringVar()
    row5e1_entry = Entry(frame5, textvariable=row5e1, width = 2,font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row5e1_entry.pack(side = LEFT, padx=5, pady=5)
    row5e2_entry = Entry(frame5, textvariable=row5e2, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row5e2_entry.pack(side = LEFT, padx=5, pady=5)
    row5e3_entry = Entry(frame5, textvariable=row5e3, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row5e3_entry.pack(side = LEFT, padx=5, pady=5)
    row5e4_entry = Entry(frame5, textvariable=row5e4, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row5e4_entry.pack(side = LEFT)
    #--- Starting Wordle Game UI for SIXTH row. ---.
    global row6e1
    global row6e2
    global row6e3
    global row6e4
    global row6e1_entry
    global row6e2_entry
    global row6e3_entry
    global row6e4_entry
    row6e1 = StringVar()
    row6e2 = StringVar()
    row6e3 = StringVar()
    row6e4 = StringVar()
    row6e1_entry = Entry(frame6, textvariable=row6e1, width = 2,font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row6e1_entry.pack(side = LEFT, padx=5, pady=5)
    row6e2_entry = Entry(frame6, textvariable=row6e2, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row6e2_entry.pack(side = LEFT, padx=5, pady=5)
    row6e3_entry = Entry(frame6, textvariable=row6e3, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row6e3_entry.pack(side = LEFT, padx=5, pady=5)
    row6e4_entry = Entry(frame6, textvariable=row6e4, width = 2, font = ('Geogia 20'), bg='black', fg='white', justify='center')
    row6e4_entry.pack(side = LEFT)
    
    #Answer submission button...
    buttonFont = font.Font(size=12, weight='bold')  #This line is to add style to button texts.
    submitButton = Button(bottomframe, text="Submit", font="buttonFont", width=10, height=1, bg="blue", fg="white")
    submitButton.pack(pady=20)
    submitButton.config(command=fnCheckAttemptNo)
    wordle_screen.mainloop()

# -------- Function to check which attempt this is ----
def fnCheckAttemptNo():

    #Using global variables to access in this function.
    global tmpLabel
    global tempCount
    global wordle_screen
    global nextlevelframe
    global tmpLabel
    #End

    #Checking attempt and then to check the user answer with final answer.
    print(f"Count = {tempCount}")
    print("Function called")
    if tempCount == 1:
        row1e1_info = row1e1_entry.get()
        row1e2_info = row1e2_entry.get()
        row1e3_info = row1e3_entry.get()
        row1e4_info = row1e4_entry.get()
        print(f"Row1E1 = {row1e1_info}")
        row1e1_entry.config(state="disabled")
        row1e2_entry.config(state="disabled")
        row1e3_entry.config(state="disabled")
        row1e4_entry.config(state="disabled")
        tmpAnswer = row1e1_info + row1e2_info + row1e3_info + row1e4_info
        print(f"tmpanswer = {tmpAnswer}")
        greenList, yellowList, greyList = WordleClass.fnStoreUserInputList(tmpAnswer)
        print(greenList)
        print(yellowList)
        print(greyList)
        #If we write loop like this, i becomes value rather than position.
        for i in greenList:
            if i==1:
                row1e1_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==2:
                row1e2_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==3:
                row1e3_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==4:
                row1e4_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
        for i in yellowList:
            if i==1:
                row1e1_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==2:
                row1e2_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==3:
                row1e3_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==4:
                row1e4_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
        for i in greyList:
            if i==1:
                row1e1_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==2:
                row1e2_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==3:
                row1e3_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==4:
                row1e4_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
        #Checking if answer is correct or not.
        if len(greenList)==4:
            tmpLabelcorrect = Label(wordle_screen, text="Congratulations! Your Answer is CORRECT.", fg="green", font=("calibri", 11))
            tmpLabelcorrect.pack()

            #Answer submission button...
            buttonFont = font.Font(size=12, weight='bold')  #This line is to add style to button texts.
            btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont", width=10, height=1, bg="dark green", fg="white")
            btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
            btnNextLevel.pack()
            btnNextLevel.config(command=fnNextLevel)
        else:
            tmpLabel = Label(wordle_screen, text="Incorrect Answer. Try Again.", fg="green", font=("calibri", 11))
            tmpLabel.pack()
            tempCount += 1
    
    #--- For second attempt ----
    elif tempCount == 2:
        row2e1_info = row2e1_entry.get()
        row2e2_info = row2e2_entry.get()
        row2e3_info = row2e3_entry.get()
        row2e4_info = row2e4_entry.get()
        row2e1_entry.config(state="disabled")
        row2e2_entry.config(state="disabled")
        row2e3_entry.config(state="disabled")
        row2e4_entry.config(state="disabled")
        tmpAnswer = row2e1_info + row2e2_info + row2e3_info + row2e4_info
        print(tmpAnswer)
        greenList, yellowList, greyList = WordleClass.fnStoreUserInputList(tmpAnswer)
        print(greenList)
        print(yellowList)
        print(greyList)
        for i in greenList:
            if i==1:
                row2e1_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==2:
                row2e2_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==3:
                row2e3_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==4:
                row2e4_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
        for i in yellowList:
            if i==1:
                row2e1_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==2:
                row2e2_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==3:
                row2e3_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==4:
                row2e4_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
        for i in greyList:
            if i==1:
                row2e1_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==2:
                row2e2_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==3:
                row2e3_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==4:
                row2e4_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
        #Checking if answer is correct or not.
        if len(greenList)==4:
            tmpLabelcorrect = Label(wordle_screen, text="Congratulations! Your Answer is CORRECT.", fg="green", font=("calibri", 11))
            tmpLabelcorrect.pack()

            #Answer submission button...
            buttonFont = font.Font(size=12, weight='bold')  #This line is to add style to button texts.
            btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont", width=10, height=1, bg="dark green", fg="white")
            btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
            btnNextLevel.pack()
            btnNextLevel.config(command=fnNextLevel)
        else:
            tmpLabel.destroy()
            tmpLabel = Label(wordle_screen, text="Incorrect Answer. Try Again.", fg="green", font=("calibri", 11))
            tmpLabel.pack()
            tempCount += 1
    
    # ----- For third attempt ------
    elif tempCount == 3:
        row3e1_info = row3e1_entry.get()
        row3e2_info = row3e2_entry.get()
        row3e3_info = row3e3_entry.get()
        row3e4_info = row3e4_entry.get()
        row3e1_entry.config(state="disabled")
        row3e2_entry.config(state="disabled")
        row3e3_entry.config(state="disabled")
        row3e4_entry.config(state="disabled")
        tmpAnswer = row3e1_info + row3e2_info + row3e3_info + row3e4_info
        print(tmpAnswer)
        greenList, yellowList, greyList = WordleClass.fnStoreUserInputList(tmpAnswer)
        print(greenList)
        print(yellowList)
        print(greyList)
        for i in greenList:
            if i==1:
                row3e1_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==2:
                row3e2_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==3:
                row3e3_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==4:
                row3e4_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
        for i in yellowList:
            if i==1:
                row3e1_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==2:
                row3e2_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==3:
                row3e3_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==4:
                row3e4_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
        for i in greyList:
            if i==1:
                row3e1_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==2:
                row3e2_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==3:
                row3e3_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==4:
                row3e4_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
        #Checking if answer is correct or not.
        if len(greenList)==4:
            tmpLabelcorrect = Label(wordle_screen, text="Congratulations! Your Answer is CORRECT.", fg="green", font=("calibri", 11))
            tmpLabelcorrect.pack()

            #Answer submission button...
            buttonFont = font.Font(size=12, weight='bold')  #This line is to add style to button texts.
            btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont", width=10, height=1, bg="dark green", fg="white")
            btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
            btnNextLevel.pack()
            btnNextLevel.config(command=fnNextLevel)
        else:
            tmpLabel.destroy()
            tmpLabel = Label(wordle_screen, text="Incorrect Answer. Try Again.", fg="green", font=("calibri", 11))
            tmpLabel.pack()
            tempCount+=1
    
    #Checking for FORTH attempt ----.
    elif tempCount == 4:
        row4e1_info = row4e1_entry.get()
        row4e2_info = row4e2_entry.get()
        row4e3_info = row4e3_entry.get()
        row4e4_info = row4e4_entry.get()
        row4e1_entry.config(state="disabled")
        row4e2_entry.config(state="disabled")
        row4e3_entry.config(state="disabled")
        row4e4_entry.config(state="disabled")
        tmpAnswer = row4e1_info + row4e2_info + row4e3_info + row4e4_info
        print(tmpAnswer)
        greenList, yellowList, greyList = WordleClass.fnStoreUserInputList(tmpAnswer)
        print(greenList)
        print(yellowList)
        print(greyList)
        for i in greenList:
            if i==1:
                row4e1_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==2:
                row4e2_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==3:
                row4e3_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==4:
                row4e4_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
        for i in yellowList:
            if i==1:
                row4e1_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==2:
                row4e2_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==3:
                row4e3_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==4:
                row4e4_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
        for i in greyList:
            if i==1:
                row4e1_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==2:
                row4e2_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==3:
                row4e3_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==4:
                row4e4_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
        #Checking if answer is correct or not.
        if len(greenList)==4:
            tmpLabelcorrect = Label(wordle_screen, text="Congratulations! Your Answer is CORRECT.", fg="green", font=("calibri", 11))
            tmpLabelcorrect.pack()

            #Answer submission button...
            buttonFont = font.Font(size=12, weight='bold')  #This line is to add style to button texts.
            btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont", width=10, height=1, bg="dark green", fg="white")
            btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
            btnNextLevel.pack()
            btnNextLevel.config(command=fnNextLevel)
        else:
            tmpLabel.destroy()
            tmpLabel = Label(wordle_screen, text="Incorrect Answer. Try Again.", fg="green", font=("calibri", 11))
            tmpLabel.pack()
            tempCount+=1
    
    #Checking for FIFTH attempt ----.
    elif tempCount == 5:
        row5e1_info = row5e1_entry.get()
        row5e2_info = row5e2_entry.get()
        row5e3_info = row5e3_entry.get()
        row5e4_info = row5e4_entry.get()
        row5e1_entry.config(state="disabled")
        row5e2_entry.config(state="disabled")
        row5e3_entry.config(state="disabled")
        row5e4_entry.config(state="disabled")
        tmpAnswer = row5e1_info + row5e2_info + row5e3_info + row5e4_info
        print(tmpAnswer)
        greenList, yellowList, greyList = WordleClass.fnStoreUserInputList(tmpAnswer)
        print(greenList)
        print(yellowList)
        print(greyList)
        for i in greenList:
            if i==1:
                row5e1_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==2:
                row5e2_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==3:
                row5e3_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==4:
                row5e4_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
        for i in yellowList:
            if i==1:
                row5e1_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==2:
                row5e2_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==3:
                row5e3_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==4:
                row5e4_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
        for i in greyList:
            if i==1:
                row5e1_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==2:
                row5e2_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==3:
                row5e3_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==4:
                row5e4_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
        #Checking if answer is correct or not.
        if len(greenList)==4:
            tmpLabelcorrect = Label(wordle_screen, text="Congratulations! Your Answer is CORRECT.", fg="green", font=("calibri", 11))
            tmpLabelcorrect.pack()

            #Answer submission button...
            buttonFont = font.Font(size=12, weight='bold')  #This line is to add style to button texts.
            btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont", width=10, height=1, bg="dark green", fg="white")
            btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
            btnNextLevel.pack()
            btnNextLevel.config(command=fnNextLevel)
        else:
            tmpLabel.destroy()
            tmpLabel = Label(wordle_screen, text="Incorrect Answer. Try Again.", fg="green", font=("calibri", 11))
            tmpLabel.pack()
            tempCount+=1

    #Checking for SIXTH attempt ----.
    elif tempCount == 6:
        row6e1_info = row6e1_entry.get()
        row6e2_info = row6e2_entry.get()
        row6e3_info = row6e3_entry.get()
        row6e4_info = row6e4_entry.get()
        row6e1_entry.config(state="disabled")
        row6e2_entry.config(state="disabled")
        row6e3_entry.config(state="disabled")
        row6e4_entry.config(state="disabled")
        tmpAnswer = row6e1_info + row6e2_info + row6e3_info + row6e4_info
        print(tmpAnswer)
        greenList, yellowList, greyList = WordleClass.fnStoreUserInputList(tmpAnswer)
        print(greenList)
        print(yellowList)
        print(greyList)
        for i in greenList:
            if i==1:
                row6e1_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==2:
                row6e2_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==3:
                row6e3_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
            if i==4:
                row6e4_entry.configure(disabledbackground="green", state="disabled", disabledforeground="black")
        for i in yellowList:
            if i==1:
                row6e1_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==2:
                row6e2_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==3:
                row6e3_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
            if i==4:
                row6e4_entry.configure(disabledbackground="yellow", state="disabled", disabledforeground="black")
        for i in greyList:
            if i==1:
                row6e1_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==2:
                row6e2_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==3:
                row6e3_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
            if i==4:
                row6e4_entry.configure(disabledbackground="grey", state="disabled", disabledforeground="black")
        #Checking if answer is correct or not.
        if len(greenList)==4:
            tmpLabelcorrect = Label(wordle_screen, text="Congratulations! Your Answer is CORRECT.", fg="green", font=("calibri", 11))
            tmpLabelcorrect.pack()

            #Answer submission button...
            buttonFont = font.Font(size=12, weight='bold')  #This line is to add style to button texts.
            btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont", width=10, height=1, bg="dark green", fg="white")
            btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
            btnNextLevel.pack()
            btnNextLevel.config(command=fnNextLevel)
        else:
            #Destroying previous label(because I can't print label six times. So destroying previous label and then overriding next label.)
            tmpLabel.destroy()
            tmpLabel = Label(wordle_screen, text="Incorrect Answer. You lose this game. No Attempts Remain.", fg="green", font=("calibri", 11))
            tmpLabel.pack()

            #Calling function to get correct answer.
            finalWord = WordleClass.getCorrectAnswer()

            #Printing correct answer.
            Label(wordle_screen, text="Correct Answer Is...", fg="blue", font=("calibri", 15)).pack()
            Label(wordle_screen, text=finalWord, fg="blue", font=("calibri", 15)).pack()

            #Answer submission button...
            buttonFont = font.Font(size=12, weight='bold')  #This line is to add style to button texts.
            btnNextLevel = Button(wordle_screen, text="Next Level", font="buttonFont", width=10, height=1, bg="dark green", fg="white")
            btnNextLevel.place(relx=0.0, rely=1.0, anchor='sw')
            btnNextLevel.pack()
            btnNextLevel.config(command=fnNextLevel)
            tempCount=1

def fnNextLevel():
    global wordle_screen
    wordle_screen.destroy()
    wordle_test()

#Calling main account function. Beginning Page.
main_account_screen()