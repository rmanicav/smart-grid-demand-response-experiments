import simpy
from utilities.connect import connectclass as c
class customerclass:
    
    def __init__(self):
        self.id=0
        self.name =''
        self.accnum = 0
        self.mnum =0
        self.dr_flag = 0
        self.phone =931-111-1111
        self.cnt_type = 1
        self.event_day = False
                
       
    def time_to_failure():
        return random.expovariate(10)

    def event_check(self,env):        
       
       configlist =[]
       
       cn = c.connect()
    # create a database connection
       conn = cn.create_connection()
       rows = cn.select_all_config(conn)
       for row in rows:
            print(row)
            configlist.append(row[0])
       while True:
            today = date.today() - 2
            d = today.strftime("%m/%d/%y")
            print("date is  =", d)
            print('Start check on event date %d' % env.now)
            config_duration = 20
            if d in configlist :
                self.event_day = True
            yield env.timeout(config_duration)
       messagebox("Sending notification to customer\n")    
       print("Notify customer of event before 2 days via phone or text message on : ", d)       
       return True
    
    