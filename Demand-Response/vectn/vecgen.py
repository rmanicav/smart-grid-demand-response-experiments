from utilities.connect import connectclass as c
import simpy 
import random
from datetime import date
class vecgenclass:
        
    def __init__(self, env):
        self.env = env
        self.meterid =0
        self.customerid =0
        self.todaydt =date.today()
           
        
    def time_to_failure():
        return random.expovariate(10)

    def read_dr_config(self,env):        
       today = date.today() - 2
       d = today.strftime("%m/%d/%y")
       print("date is  =", d)
       configlist =[]
       
       cn = c.connect()
    # create a database connection
       conn = cn.create_connection()
       rows = cn.select_all_config(conn)
       for row in rows:
            print(row)
            configlist.append(row[0])
       while True or d not in configlist:
            print('Start reading config file %d' % env.now)
            config_duration = 20
            yield env.timeout(config_duration)
            
       print("Notify customer of event before 2 days: ", d)       
       return True
       
            
    def gen_billing_dt(self,env):
        configlist =[]
        cn = c.connect()
    # create a database connection
        conn = cn.create_connection()
        rows = cn.select_bill_config(conn)
        for row in rows:
            print(row)
            configlist.append(row[0])
        while True or d not in configlist:
            today = date.today() - 2
            d = today.strftime("%m/%d/%y")
            print("date is  =", d)
            print('Start reading billing date %d' % env.now)
            config_duration = 10
            yield env.timeout(config_duration)            
        print("Notify VEN to generate bill for the month: ", d)                    
        return True
        
   
def main():
 
  env = simpy.Environment() 
  v = vecgen(env)
    
  env.process(v.read_dr_config(env))    
  env.process(v.gen_billing_dt(env))   
    
if __name__ == '__main__':
    main()

       
    
    