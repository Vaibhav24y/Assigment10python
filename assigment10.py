import tkinter as tk
import webbrowser as wb
obj=tk.Tk(className="Youtube ")
e=tk.Entry(obj,  font=("Times New Roman",25),width=30) 
e.grid()
def display():
    s=e.get()
    print(s)
    wb.open("https://www.youtube.com/"+s)
    print("Website Navigator")
b=tk.Button(obj,text="Button",font=("Times New Roman",30),command=display)
b.grid(row=1,column=1)
obj.mainloop()
