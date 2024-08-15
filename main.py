from tkinter import *
import backend
from tkinter import ttk

library=backend.Library()

root= Tk()
root.geometry('435x600')

nameIn=ttk.Entry(root)
yearIn=ttk.Entry(root)
authorIn=ttk.Entry(root)

addbook = ttk.Button(root,text='Add Book',command= lambda:library.Add_book(nameIn.get(),int(yearIn.get()),authorIn.get()))

nameIn.grid(row=0,column=0,padx=10,pady=10)
yearIn.grid(row=0,column=1,padx=10,pady=10)
authorIn.grid(row=0,column=2,padx=10,pady=10)
addbook.grid(row=1,column=0,columnspan=3,pady=10)




root.mainloop()