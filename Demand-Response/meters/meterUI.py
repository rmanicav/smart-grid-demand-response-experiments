
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
#import pandas as pd
import connect as c
import csv


class meterUI:
   
   def UploadAction(event=None):
      filename = filedialog.askopenfilename()      
      messagebox.showinfo("Uploading File... ", filename)
      print('Read meter data from csv')
      #'Data\\2021Customer.csv'
      with open(filename,'r') as fin:
         dr = csv.DictReader(fin)
         to_db = [(i['met_num'],i['name'],i['acc_num'],i['actv_dt'],i['start_dt'],i['end_dt'],i['cycle'],i['voltage'],i['nomination']) for i in dr]      
      
      con=c.connect()      
      conn = con.create_connection()
      cur = conn.cursor()
      sql = ''' INSERT INTO meter (met_num,name,acc_num,actv_dt,start_dt,end_dt,cycle,voltage,nomination)
                  VALUES (?,?,?,?,?,?,?,?,?); '''
                  
      cur.executemany(sql, to_db)
      conn.commit()
      conn.close()
      messagebox.showinfo("Meter records inserted")
     
   def insert_meter(meterData):
               
    conn=c.connect()
    # create a database connection
    conn = conn.create_connection()
    conn.insert_meter(conn,meterData)     
    
   def update_meter(meterData):
               
    conn=c.connect()
    # create a database connection
    conn = conn.create_connection()
    conn.update_meter(conn,meterData)         
     
   

   window = tk.Tk("Meter")
   window.geometry("400x200")
   mainlabel = tk.Label(text="Meter Information")
   mainlabel.pack()
   filelabel = tk.Label(text="File Information")
   filelabel.pack()
   ubutton = tk.Button(window, text='Upload and Save File', command=UploadAction)
   ubutton.pack()   

   
   window.mainloop()


''' 
def saveCallBack():
      msg = messagebox.showinfo( "Hello Python", "Hello World")
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
   
                           

   B = Button(window, text = "Save", command = saveCallBack)

   mainlabel.pack()

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
   
   save = Button(window, text = "Save", command = saveCallBack)
   save.place(x = 325,y = 325)
'''
   
   
