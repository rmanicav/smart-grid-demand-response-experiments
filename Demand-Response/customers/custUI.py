import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
#import pandas as pd
import connect as c
import csv

class customerUI:
   
   def UploadAction():
      filename = filedialog.askopenfilename()      
      messagebox.showinfo("Uploading File... ", filename)
      print('Read customer data from csv')
      #'Data\\2021Customer.csv'
      with open(filename,'r') as fin:
         dr = csv.DictReader(fin)
         to_db = [(i['name'],i['meterid'],i['accountnum'],i['phonenumber'],i['cnttype'],i['drflag']) for i in dr]      
      
      con=c.connect()      
      conn = con.create_connection()
      cur = conn.cursor()
      sql = ''' INSERT INTO customer(name,meter_id,account_num,phone_number,cnt_type,dr_flag) VALUES (?,?,?,?,?,?); '''
      cur.executemany(sql, to_db)
      conn.commit()
      conn.close()
      messagebox.showinfo("Customer records inserted")
      
   def insert_customer(custdata):
           
      con=c.connect()
    # create a database connection
      conn = con.create_connection()
      con.insert_customer(conn,custdata)

   def update_customer(custData):
      con=c.connect()
    # create a database connection
      conn = con.create_connection()
      con.update_customer(conn,custdata) 

   window = tk.Tk("Customer")
   window.geometry("400x200")

   mainlabel = tk.Label(text="Customer Information")
   mainlabel.pack()
   filelabel = tk.Label(text="File Information")
   filelabel.pack()
   ubutton = tk.Button(window, text='Upload and Save File', command=UploadAction)
   ubutton.pack()   
   
   window.mainloop()
   
   '''
   namelabel = tk.Label(text="Name")
   entry = tk.Entry()
   name = entry.get()

   meterlabel = tk.Label(text="Meter Number")
   mentry = tk.Entry()
   meter = mentry.get()

   accountnumlabel=tk.Label(text="Account Number")
   aentry = tk.Entry()
   accnum = mentry.get()

   phonenumberlabel=tk.Label(text="Phone Number")
   pentry = tk.Entry()
   phonenumber = pentry.get()

   cnttypelabel =label=tk.Label(text="Contact type")
   centry = tk.Entry()
   cnttype = centry.get()
   
   drflaglabel =label=tk.Label(text="DR")
   dentry = tk.Entry()
   drflag = dentry.get()
                      

   mainlabel.pack()

   namelabel.pack()
   entry.pack()

   meterlabel.pack()
   mentry.pack()

   accountnumlabel.pack()
   aentry.pack()

   phonenumberlabel.pack()
   pentry.pack()

   cnttypelabel.pack()
   centry.pack()

   drflaglabel.pack()
   dentry.pack()

   #filelabel = tk.Label(window,text='File path')
   #filelabel.pack()
''' 

