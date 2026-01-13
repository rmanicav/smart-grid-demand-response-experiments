import pandas as pd
import simpy 
   
 
class meterclass:
    
    """
    """
    def __init__(self):
        self.mnum = 0
        self.accnum = 0
        self.cycle =6
        self.nomination = 0
        self.voltage =10
        self.dr_flag = 0
        self.vol =0  
        self.event_day = False
        self.customerid =0
        
        
    """[summary]
    """    
    def meterRead(self):
        meterdata =[]
        print('Read meter reading from csv')
        df = pd.read_csv('Data\\2021-meterdata.csv', delimiter=',')
        columnsNamesArr = df.columns.values
        print(columnsNamesArr)
        meterdata = df.values.tolist()
        meterdata.append(meterdata)
        
        print(meterdata[0])
                
        return meterdata
    
       
    def time_to_failure():
        return random.expovariate(10)

    def event_check(self,env):        
       configlist =[]
       
       cn = c.connect()
    # create a database connection
       conn = cn.create_connection(database)
       rows = cn.select_all_config(conn)
       d = today.strftime("%m/%d/%y")
       
       for row in rows:
            print(row)
            configlist.append(row[0])
       while True and d not in configlist:
            today = date.today() - 2            
            print("date is  =", d)
            print('Start reading config file %d' % env.now)
            config_duration = 20
            yield env.timeout(config_duration)
       self.event_day =True
       print("Notify customer of event before 2 days via phone or text message on : ", d)       
       return self.event_day

m = meterclass()
m.meterRead()
