import tkinter as tk
from tkinter import *

from tkinter import messagebox

class importexcel:
   
   def saveCallBack():
      msg = messagebox.showinfo( "Hello Python", "Hello World")

   window = tk.Tk("Import Excel Data")
   window.geometry("400x400")

   mainlabel = tk.Label(text="Import Excel Data")

   namelabel = tk.Label(text="File Name")
   entry = tk.Entry()
   name = entry.get()

   B = Button(window, text = "Save", command = saveCallBack)

   B.place(x = 350,y = 250)

   namelabel.pack()
   entry.pack()

   window.mainloop()
