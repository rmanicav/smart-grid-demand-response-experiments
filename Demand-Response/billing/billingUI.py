import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
#import pandas as pd
import connect as c
import csv

class billingUI:
    def genBilling():
      return true

window = tk.Tk("Customer Billing Information")
window.geometry("400x200")
mainlabel = tk.Label(text="Customer Billing Information")
mainlabel.pack()
filelabel = tk.Label(text="Customer#")
filelabel.pack()
ubutton = tk.Button(window, text='Get Billing for Customer', command=genBilling())
ubutton.pack()   
window.mainloop()
    
