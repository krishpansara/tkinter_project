from tkinter import *
root = Tk()
root.title("Calculator")
#icon
root.iconbitmap('F:/Download/calc.ico')

ent = Entry(root ,width = 20, borderwidth = 3, font = ('Arial 24'))
ent.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)
# ent.pack(padx = 30, pady=10)

def button_click(number):
    current = ent.get()
    ent.delete(0, END)
    ent.insert(0, str(current) + str(number))

# def dot_click():
#     current = ent.get()
#     ent.delete(0, END)
#     ent.insert(0, float(current + '.' ))

def add_num():
    first_number = ent.get()
    global f_num 
    global operation 
    operation = 'Addition'
    f_num = int(first_number)
    ent.delete(0, END)

def sub_num():
    first_number = ent.get()
    global f_num
    global operation 
    operation = 'substration'
    f_num = int(first_number)
    ent.delete(0, END)

def mult_num():
    first_number = ent.get()
    global f_num 
    global operation 
    operation = 'multiplication'
    f_num = int(first_number)
    ent.delete(0, END)

def div_num():
    first_number = ent.get()
    global f_num 
    global operation 
    operation = 'divison'
    f_num = int(first_number)
    ent.delete(0, END)


def equal():
    if operation == 'Addition':
        sec_num = ent.get()
        ent.delete(0,END)
        ent.insert(0,f_num + int(sec_num))

    if operation == 'substration':
        sec_num = ent.get()
        ent.delete(0,END)
        ent.insert(0,f_num - int(sec_num))
    
    if operation == 'multiplication':
        sec_num = ent.get()
        ent.delete(0,END)
        ent.insert(0,f_num * int(sec_num))

    if operation == 'divison':
        sec_num = ent.get()
        ent.delete(0,END)
        ent.insert(0,f_num / int(sec_num))

def clear_All():
    ent.delete(0, END)

def c_num():
    ent.delete(1, END)

# creating button
button1 = Button(root, text = '1', padx = 40, pady = 20, bg = "White", command = lambda: button_click(1))
button2 = Button(root, text = '2', padx = 40, pady = 20, bg = "White", command = lambda: button_click(2))
button3 = Button(root, text = '3', padx = 40, pady = 20, bg = "White", command = lambda: button_click(3))
button4 = Button(root, text = '4', padx = 40, pady = 20, bg = "White", command = lambda: button_click(4))
button5 = Button(root, text = '5', padx = 40, pady = 20, bg = "White", command = lambda: button_click(5))
button6 = Button(root, text = '6', padx = 40, pady = 20, bg = "White", command = lambda: button_click(6))
button7 = Button(root, text = '7', padx = 40, pady = 20, bg = "White", command = lambda: button_click(7))
button8 = Button(root, text = '8', padx = 40, pady = 20, bg = "White", command = lambda: button_click(8))
button9 = Button(root, text = '9', padx = 40, pady = 20, bg = "White", command = lambda: button_click(9))
button0 = Button(root, text = '0', padx = 88, pady = 20, bg = "White", command = lambda: button_click(0))
button_dot = Button(root, text = '.', padx = 41, pady = 20, bg = "White")

button_mult = Button(root, text = "*", padx = 40, pady = 20, bg = "LightGray", command = mult_num)
button_subst = Button(root, text = "-", padx = 40, pady = 20, bg = "LightGray", command = sub_num)
button_sum = Button(root, text = "+", padx = 39, pady = 55, bg = "LightGray", command = add_num)
button_equal = Button(root, text = "=", padx = 38, pady = 20, bg = "LightBlue", command = equal)
button_div = Button(root, text = "/",padx = 40, pady = 20, bg = "LightGray", command = div_num)
button_clear = Button(root, text = "AC",padx = 35, pady = 20, bg = "LightGray", command = clear_All)
button_per = Button(root, text = "C",padx = 38, pady = 20, bg = "LightGray", command = c_num)

# showing button
button_clear.grid(row = 1, column = 0)
button_per.grid(row = 1, column = 1)
button_div.grid(row = 1, column = 2)

button1.grid(row = 4, column = 0)
button2.grid(row = 4, column = 1)
button3.grid(row = 4, column = 2)
button_mult.grid(row = 1,column = 3)
button_sum.grid(row = 3,column = 3,rowspan = 2)

button4.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)
button_subst.grid(row =2,column = 3)

button7.grid(row = 2, column = 0)
button8.grid(row = 2, column = 1)
button9.grid(row = 2, column = 2)

button0.grid(row = 5, column = 0, columnspan = 2)
button_dot.grid(row = 5, column = 2, columnspan = 1)
button_equal.grid(row = 5, column = 3)

root.mainloop()