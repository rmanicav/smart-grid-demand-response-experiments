import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
#import pandas as pd
import connect as c
import csv

class eventdataUI:
     def genEventData():
      return true
    

window = tk.Tk("Event Data")
window.geometry("400x200")
mainlabel = tk.Label(text="Event Information")
mainlabel.pack()
filelabel = tk.Label(text="Customer#:")
filelabel.pack()
ubutton = tk.Button(window, text='Get event Data', command=genEventData())
ubutton.pack()   

window.mainloop()