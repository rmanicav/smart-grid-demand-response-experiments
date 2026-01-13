import sqlite3
from sqlite3 import Error
db_file = r"C:\sqlite\sqlite-tools-win32-x86-3370000\DR.db"
class connectclass:
    
  def create_connection(self):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

  def select_all_config(self,conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT config_val FROM config where config_type ='event_dt'")
    rows = cur.fetchall()

    for row in rows:
        print(row[0])
    
    return rows
    
  def select_bill_config(self,conn):
    cur = conn.cursor()
    cur.execute("SELECT config_val FROM config where config_type ='bill_dt'")
    rows = cur.fetchall()
    for row in rows:
        print(row[0])
          
    return rows
      
  def select_all_meter(self,conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM meter")

    rows = cur.fetchall()

    for row in rows:
        print(row)
        
    return rows
        
  def insert_meter(self,conn,meterdata):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO meter (met_num,name,acc_num,actv_dt,start_dt,end_dt,cycle,voltage)
                  VALUES (?,?,?,?,?,?,?,?); '''
                  
    cur = conn.cursor()
    cur.execute(sql,meterdata)
    conn.commit()
    return cur.lastrowid

  def insert_customer(self,conn,custdata):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO customer(name,meter_id,account_num,phone_number,cnt_type,dr_flag) VALUES (?,?,?,?,?,?); '''
    cur = conn.cursor()
    cur.execute(sql,custdata)
    conn.commit()
    return cur.lastrowid

  def gen_report(self,conn,customerid):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM event")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
        
    return rows

  def update_customer(self,conn,customerdata):
    sql = '''UPDATE customer
    SET customer_id = 'customer_id',
       name = 'name',
       meter_id = 'meter_id',
       account_num = 'account_num',
       phone_number = 'phone_number',
       cnt_type = 'cnt_type',
       dr_flag = 'dr_flag'
    WHERE customer_id = 'customer_id' '''

    cur = conn.cursor()
    cur.execute(sql,custdata)
    conn.commit()
    return cur.lastrowid
    
  
  def update_meter(self,conn,meterdata):
    sql ='''UPDATE meter
           SET id = 'id',
       met_num = 'met_num',
       name = 'name',
       acc_num = 'acc_num',
       actv_dt = 'actv_dt',
       start_dt = 'start_dt',
       end_dt = 'end_dt',
       cycle = 'cycle',
       voltage = 'voltage',
      
     WHERE id = 'id' AND 
       met_num = 'met_num' '''

    cur = conn.cursor()
    cur.execute(sql,custdata)
    conn.commit()
    return cur.lastrowid 
def main():
    
    
    c = connect()
    # create a database connection
    conn = c.create_connection(db_file)
    c.select_all_config(conn)
    c.select_bill_config(conn)
    
    


if __name__ == '__main__':
    main()
