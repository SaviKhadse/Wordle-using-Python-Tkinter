#import modules

from ctypes.wintypes import SIZE
from tkinter import *
import os
from tkinter import messagebox
from tkinter import font

# importing database class from file name called "testdbfile_tkinter"
from tkinter_dbconnection_file import mysqlCon
mysqlCon.fndbconn()
# Designing window for registration


def register():
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

    global username
    global password
    global tmpemail
    global username_entry
    global password_entry
    global email_entry
    username = StringVar()
    password = StringVar()
    tmpemail = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue",
          fg="white", width="300", height="2", font=("Calibri", 13)).pack()
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

    # This line is to add style to button texts.
    buttonFont = font.Font(size=12, weight='bold')
    Button(register_screen, text="Register", font="buttonFont", width=10,
           height=1, bg="blue", fg="white", command=register_user).pack()

# Designing window for login.


def login():
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
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()

    # This line is to add style to button texts.
    buttonFont = font.Font(size=12, weight='bold')
    Button(login_screen, font="buttonFont", text="Login", bg="blue",
           fg="white", width=10, height=1, command=login_verify).pack()

# Implementing event on register button


def register_user():

    username_info = username.get()  # Get text is used to get the value from the Python Tkinter entry widget. In other words, Get text pulls whatever value is provided by the user. If you want to use the value that is provided by the user, then get the text is used
    password_info = password.get()
    email_info = tmpemail.get()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)

    checkUser = mysqlCon.fnRegister(username_info, password_info, email_info)

    Label(register_screen, text="Registration Success",
          fg="green", font=("calibri", 11)).pack()

# Implementing event on login button


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    checkUser = mysqlCon.fnLogin(username1, password1)

    if len(checkUser) > 0:
        wordle()
    else:
        password_not_recognised()

# Designing popup for login success


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK",
           command=delete_login_success).pack()

# Designing popup for login invalid password


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",
           command=delete_password_not_recognised).pack()

# Designing popup for user not found


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK",
           command=delete_user_not_found_screen).pack()

# Deleting popups


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing main WORDLE game UI.
def wordle():
    global wordle_screen
    wordle_screen = Toplevel(main_screen)
    wordle_screen.title("Wordle Game Main Screen")
    wordle_screen.geometry("350x500")

    # Added for Wordle....
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

    bottomframe = Frame(wordle_screen)
    bottomframe.pack()

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
    # End of wordle UI....

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

    Label(iframe, text="Please enter details below", bg="blue",
          fg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(iframe, text="").pack()

    row1e1_entry = Entry(frame1, textvariable=row1e1, width=2, font=(
        'Geogia 20'), bg='black', fg='white', justify='center')
    row1e1_entry.pack(side=LEFT, padx=3)
    row1e2_entry = Entry(frame1, textvariable=row1e2, width=2, font=(
        'Geogia 20'), bg='black', fg='white', justify='center')
    row1e2_entry.pack(side=LEFT, padx=3)
    row1e3_entry = Entry(frame1, textvariable=row1e3, width=2, font=(
        'Geogia 20'), bg='black', fg='white', justify='center')
    row1e3_entry.pack(side=LEFT, padx=3)
    row1e4_entry = Entry(frame1, textvariable=row1e4, width=2, font=(
        'Geogia 20'), bg='black', fg='white', justify='center')
    row1e4_entry.pack(side=LEFT)
    row1e5_entry = Entry(frame1, textvariable=row1e5, width=2, font=(
        'Geogia 20'), bg='black', fg='white', justify='center')
    row1e5_entry.pack(side=LEFT)

    #username_entry = Entry(wordle_screen, textvariable=username)
    # username_entry.pack()

    # This line is to add style to button texts.
    buttonFont = font.Font(size=12, weight='bold')
    Button(bottomframe, text="Submit", font="buttonFont", width=10,
           height=1, bg="white", fg="blue", command=register_user).pack()


# Designing Main(first) window

def main_account_screen():
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
           width="20", bg="blue", fg="black", command=login).pack()
    Label(text="").pack()
    button = Button(text="Register", font="buttonFont", height="2",
                    width="20", bg="blue", fg="black", command=register).pack()
    main_screen.mainloop()


main_account_screen()
