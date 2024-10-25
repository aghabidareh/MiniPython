import tkinter as tk
from tkinter import messagebox

def login():
    username = entry1.get()
    password = entry2.get()
    
    if (username == "" and password==""):
        messagebox.showinfo("" , "Blank Not Allowed")
    
    elif (username=="Aghabidareh" and password=="aghabidareh"):
        messagebox.showinfo("" , "You Are LogedIn Now")
        
    else:
        messagebox.showinfo("" , "Incorrect Username or Password")

root = tk.Tk()
root.title('Aghabidareh \t | \t Login')
root.geometry('300x200')
root.resizable(False , False)

global entry1
global entry2

tk.Label(root, text="Usesrname").place(x=20,y=20)
tk.Label(root, text="Password").place(x=20,y=70)


entry1 = tk.Entry(root , bd=5)
entry1.place(x=140,y=20)

entry2 = tk.Entry(root , bd=5)
entry2.place(x=140,y=70)

tk.Button(root, text="Submit" , command=login , height=3 , width=13 , bd=6).place(x=100,y=120)

root.mainloop()