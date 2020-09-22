from tkinter import *

# ! Creating a Calculator Window

root = Tk()
root.title("Calculator")
root.geometry("450x400")
root.iconbitmap("icon.ico")
root.configure(bg='#184651')

# ! Creating an input

input = Entry(root, width=50, borderwidth=2)
input.grid(row=0, column=0, columnspan=4, rowspan=2, padx=40, pady=20, ipadx=3, ipady=3)
# input.configure(font=("Poppins", 16, "normal"))

# ! Creating all required functions

def btn_click(number):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(number))


def btn_clr():
    input.delete(0, END)


def btn_add():
    global action
    action = "add"
    f_num = input.get()
    global first_number
    first_number = int(f_num)
    input.delete(0, END)


def btn_sub():
    global action
    action = "sub"
    f_num = input.get()
    global first_number
    first_number = int(f_num)
    input.delete(0, END)


def btn_mult():
    global action
    action = "mult"
    f_num = input.get()
    global first_number
    first_number = int(f_num)
    input.delete(0, END)


def btn_div():
    global action
    action = "div"
    f_num = input.get()
    global first_number
    first_number = int(f_num)
    input.delete(0, END)


def btn_eql():
    s_num = input.get()
    input.delete(0, END)

    # ! Checking the action which user wants to perform

    if action == "add":
        input.insert(0, first_number + int(s_num))
    if action == "sub":
        input.insert(0, first_number - int(s_num))
    if action == "mult":
        input.insert(0, first_number * int(s_num))
    if action == "div":
        input.insert(0, first_number / int(s_num))


# ! Creating all the Numeric Buttons

btn_1 = Button(root, text="1", padx=38, pady=0, bg="#184651", fg="#ffffff", command=lambda: btn_click(1))
btn_2 = Button(root, text="2", padx=35, pady=0, bg="#184651", fg="#ffffff", command=lambda: btn_click(2))
btn_3 = Button(root, text="3", padx=35, pady=0, bg="#184651", fg="#ffffff", command=lambda: btn_click(3))
btn_4 = Button(root, text="4", padx=35, pady=0, bg="#184651", fg="#ffffff", command=lambda: btn_click(4))
btn_5 = Button(root, text="5", padx=35, pady=0, bg="#184651", fg="#ffffff", command=lambda: btn_click(5))
btn_6 = Button(root, text="6", padx=35, pady=0, bg="#184651", fg="#ffffff", command=lambda: btn_click(6))
btn_7 = Button(root, text="7", padx=35, pady=0, bg="#184651", fg="#ffffff", command=lambda: btn_click(7))
btn_8 = Button(root, text="8", padx=35, pady=0, bg="#184651", fg="#ffffff", command=lambda: btn_click(8))
btn_9 = Button(root, text="9", padx=35, pady=0, bg="#184651", fg="#ffffff", command=lambda: btn_click(9))
btn_0 = Button(root, text="0", padx=35, pady=0, bg="#184651", fg="#ffffff", command=lambda: btn_click(0))
btn_00 = Button(root, text="00", padx=28, pady=0, bg="#184651", fg="#ffffff", command=lambda: btn_click(00))

# ! Creating  all the Functional Buttons

btn_clr = Button(root, text="Clear", padx=124.5, pady=0, bg="#12EAD0", fg="#000000", command=btn_clr)
btn_eql = Button(root, text="=", padx=96.5, pady=0, bg="#12EAD0", fg="#000000", command=btn_eql)
btn_add = Button(root, text="+", padx=43, pady=0, bg="#1A6F82", fg="#ffffff", command=btn_add)
btn_sub = Button(root, text="-", padx=45, pady=0, bg="#1A6F82", fg="#ffffff", command=btn_sub)
btn_mult = Button(root, text="*", padx=45, pady=0, bg="#1A6F82", fg="#ffffff", command=btn_mult)
btn_div = Button(root, text="/", padx=45, pady=0, bg="#1A6F82", fg="#ffffff", command=btn_div)

# ! Placing buttons on the window using Grid System

btn_1.grid(row=5, column=0)
btn_1.configure(font=("Poppins", 16, "normal"))
btn_2.grid(row=5, column=1)
btn_2.configure(font=("Poppins", 16, "normal"))
btn_3.grid(row=5, column=2)
btn_3.configure(font=("Poppins", 16, "normal"))

btn_4.grid(row=4, column=0)
btn_4.configure(font=("Poppins", 16, "normal"))
btn_5.grid(row=4, column=1)
btn_5.configure(font=("Poppins", 16, "normal"))
btn_6.grid(row=4, column=2)
btn_6.configure(font=("Poppins", 16, "normal"))

btn_7.grid(row=3, column=0)
btn_7.configure(font=("Poppins", 16, "normal"))
btn_8.grid(row=3, column=1)
btn_8.configure(font=("Poppins", 16, "normal"))
btn_9.grid(row=3, column=2)
btn_9.configure(font=("Poppins", 16, "normal"))

btn_0.grid(row=6, column=0)
btn_0.configure(font=("Poppins", 16, "normal"))
btn_00.grid(row=6, column=1)
btn_00.configure(font=("Poppins", 16, "normal"))

btn_clr.grid(row=2, column=0, columnspan=3)
btn_clr.configure(font=("Poppins", 16, "normal"))
btn_eql.grid(row=6, column=2, columnspan=2)
btn_eql.configure(font=("Poppins", 16, "normal"))
btn_add.grid(row=4, column=3)
btn_add.configure(font=("Poppins", 16, "normal"))
btn_sub.grid(row=5, column=3)
btn_sub.configure(font=("Poppins", 16, "normal"))
btn_mult.grid(row=3, column=3)
btn_mult.configure(font=("Poppins", 16, "normal"))
btn_div.grid(row=2, column=3)
btn_div.configure(font=("Poppins", 16, "normal"))

root.mainloop()
