import tkinter as tk
from turtle import end_fill

root = tk.Tk()
E1 = tk.Entry(root, width=25)
E1.grid(row=0, column=0, columnspan=3)

def button_click(n):
    current = E1.get()
    E1.delete(0 ,tk.END)
    E1.insert(0, str(current) + str(n))

def Button_Clear():
    E1.delete(0, tk.END)

def Button_add():
    first_number = E1.get()
    global f_number
    f_number = int(first_number)
    E1.delete(0, tk.END)

def Button_Equals():
    second_number = E1.get()
    E1.delete(0, tk.END)
    E1.insert(0, f_number + int(second_number))



B_1 =tk.Button(root, text="1", padx=10, pady=10, command=lambda:button_click(1))
B_2 =tk.Button(root, text="2", padx=10, pady=10, command=lambda:button_click(2))
B_3 =tk.Button(root, text="3", padx=10, pady=10, command=lambda:button_click(3))
B_4=tk.Button(root, text="4", padx=10, pady=10, command=lambda:button_click(4))
B_5 =tk.Button(root, text="5", padx=10, pady=10, command=lambda:button_click(5))
B_6 =tk.Button(root, text="6", padx=10, pady=10, command=lambda:button_click(6))
B_7 =tk.Button(root, text="7", padx=10, pady=10, command=lambda:button_click(7))
B_8 =tk.Button(root, text="8", padx=10, pady=10, command=lambda:button_click(8))
B_9 =tk.Button(root, text="9", padx=10, pady=10, command=lambda:button_click(9))
B_0 =tk.Button(root, text="0", padx=10, pady=10, command=lambda:button_click(0))

B_CLEAR = tk.Button(root, text="C", padx=15, pady=10, command=Button_Clear)
B_ADD = tk.Button(root, text="+", padx=10, pady=10, command=Button_add)
F_EQUALS = tk.Button(root, text="=", padx=10, pady=10, command=Button_Equals)



B_1.grid(row=3,column=2)
B_2.grid(row=3,column=1)
B_3.grid(row=3,column=0)

B_4.grid(row=2,column=2)
B_5.grid(row=2,column=1)
B_6.grid(row=2,column=0)

B_7.grid(row=1,column=2)
B_8.grid(row=1,column=1)
B_9.grid(row=1,column=0)

B_0.grid(row=4,column=0)

B_CLEAR.grid(row=4, column=3)
B_ADD.grid(row=4, column=2)
F_EQUALS.grid(row=4, column=1)



root.mainloop()
