from itertools import count
from tkinter import END, Label, messagebox

#Importing wordle_program_class and using methods of that program.
from tkinter_wordle_game_main_loagical_program import WordleClass

global tempCount    #This variable to call word to check as per the attempts.
tempCount = 1

# -------- Function to check which attempt this is ----
def fnCheckAttemptNo():
    global tempCount
    print("Function called")

    if tempCount == 1:
        row1e1_info = row1e1.get()
        row1e2_info = row1e2.get()
        row1e3_info = row1e3.get()
        row1e4_info = row1e4.get()

        row1e1_entry.config(state="disabled")
        row1e2_entry.config(state="disabled")
        row1e3_entry.config(state="disabled")
        row1e4_entry.config(state="disabled")

        tmpAnswer = row1e1_info + row1e2_info + row1e3_info + row1e4_info
        print(tmpAnswer)

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
            messagebox.showinfo("Success", "Your answer is correct!")
        else:
            messagebox.showwarning("Warning", "Incorrcet Answer...")
            tempCount += 1
    
    #--- For second attempt ----
    elif tempCount == 2:
        row2e1_info = row2e1.get()
        row2e2_info = row2e2.get()
        row2e3_info = row2e3.get()
        row2e4_info = row2e4.get()

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
            messagebox.showinfo("Success", "Your answer is correct!")
        else:
            messagebox.showwarning("Warning", "Incorrcet Answer...")
            tempCount += 1

    # ----- For third attempt ------
    elif tempCount == 3:
        row3e1_info = row3e1.get()
        row3e2_info = row3e2.get()
        row3e3_info = row3e3.get()
        row3e4_info = row3e4.get()

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
            messagebox.showinfo("Success", "Your answer is correct!")
        else:
            messagebox.showwarning("Warning", "Incorrcet Answer...")
            tempCount+=1
    
    #Checking for FORTH attempt ----.
    elif tempCount == 4:
        row4e1_info = row4e1.get()
        row4e2_info = row4e2.get()
        row4e3_info = row4e3.get()
        row4e4_info = row4e4.get()

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
            messagebox.showinfo("Success", "Your answer is correct!")
        else:
            messagebox.showwarning("Warning", "Incorrcet Answer...")
            tempCount+=1
            Label(wordle_screen, text="Answer Checked.", fg="green", font=("calibri", 11)).pack()
    
    #Checking for FIFTH attempt ----.
    elif tempCount == 5:
        row5e1_info = row5e1.get()
        row5e2_info = row5e2.get()
        row5e3_info = row5e3.get()
        row5e4_info = row5e4.get()

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
            messagebox.showinfo("Success", "Your answer is correct!")
        else:
            messagebox.showwarning("Warning", "Incorrcet Answer...")
            tempCount+=1
            Label(wordle_screen, text="Answer Checked.", fg="green", font=("calibri", 11)).pack()
    
    #Checking for SIXTH attempt ----.
    elif tempCount == 6:
        row6e1_info = row6e1.get()
        row6e2_info = row6e2.get()
        row6e3_info = row6e3.get()
        row6e4_info = row6e4.get()

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
            messagebox.showinfo("Success", "Your answer is correct!")
        else:
            messagebox.showwarning("Warning", "Incorrcet Answer...")
            tempCount=1

            #Clearing all data because user lost the game.
            row1e1_entry.delete(0, END)
            row1e2_entry.delete(0, END)
            row1e3_entry.delete(0, END)
            row1e4_entry.delete(0, END)

            row2e1_entry.delete(0, END)
            row2e2_entry.delete(0, END)
            row2e3_entry.delete(0, END)
            row2e4_entry.delete(0, END)

            row3e1_entry.delete(0, END)
            row3e2_entry.delete(0, END)
            row3e3_entry.delete(0, END)
            row3e4_entry.delete(0, END)

            row4e1_entry.delete(0, END)
            row4e2_entry.delete(0, END)
            row4e3_entry.delete(0, END)
            row4e4_entry.delete(0, END)

            row5e1_entry.delete(0, END)
            row5e2_entry.delete(0, END)
            row5e3_entry.delete(0, END)
            row5e4_entry.delete(0, END)

            row6e1_entry.delete(0, END)
            row6e2_entry.delete(0, END)
            row6e3_entry.delete(0, END)
            row6e4_entry.delete(0, END)

            Label(wordle_screen, text="You lose this game. No Attempts Remain.", fg="green", font=("calibri", 11)).pack()

#----- Main wordle game UI for every attemts ------.
def wordle_test():
    from tkinter import LEFT, RIGHT, Button, Entry, Frame, Label, StringVar, Tk, Toplevel, font

    global submitButton
    global wordle_screen
    wordle_screen = Tk()
    wordle_screen.title("Wordle Game Main Screen")
    wordle_screen.geometry("400x600")

    #---Frames are added ---.
    topframe = Frame(wordle_screen)
    topframe.pack()
    mframe = Frame(wordle_screen)
    mframe.pack()
    iframe = Frame(wordle_screen)
    iframe.pack()
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

    L1=Label(iframe, font=("Apple, 10"))
    L1.pack()
    L1=Label(topframe, text="W", font=("Apple, 25"), bg="#8FDE21", width=2)
    L2=Label(topframe, text="O", font=("Apple, 25"), bg="#8FDE21", width=2)
    L3=Label(topframe, text="R", font=("Apple, 25"), bg="#8FDE21", width=2)
    L4=Label(topframe, text="D", font=("Apple, 25"), bg="#8FDE21", width=2)
    L5=Label(topframe, text="L", font=("Apple, 25"), bg="#8FDE21", width=2)
    L6=Label(topframe, text="E", font=("Apple, 25"), bg="#8FDE21", width=2)
    L6.pack(side = RIGHT, padx=3, pady=20)
    L5.pack(side = RIGHT, padx=3)
    L4.pack(side = RIGHT, padx=3)
    L3.pack(side = RIGHT, padx=3)
    L2.pack(side = RIGHT, padx=3)
    L1.pack(side = RIGHT, padx=3)
    L1=Label(mframe, font=("Apple, 10"))
    L1.pack()

    Label(iframe, text="Please enter details below", bg="blue", fg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(iframe, text="").pack()
    
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

wordle_test()