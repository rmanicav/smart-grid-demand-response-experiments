
import tkinter as tk
from tkinter import *

from tkinter import messagebox

class eventUI:

   def saveCallBack():
      msg = messagebox.showinfo( "Hello Python", "Hello World")

   window = tk.Tk("Event")
   window.geometry("400x400")

   mainlabel = tk.Label(text="Event Information")

   namelabel = tk.Label(text="Event Name")
   entry = tk.Entry()
   name = entry.get()

   meterlabel = tk.Label(text="Event Date")
   mentry = tk.Entry()
   meter = mentry.get()
                  

   B = Button(window, text = "Save", command = saveCallBack)

   mainlabel.pack()

   namelabel.pack()
   entry.pack()

   meterlabel.pack()
   mentry.pack()




   B.place(x = 350,y = 250)

   window.mainloop()

