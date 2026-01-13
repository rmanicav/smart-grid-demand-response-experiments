import pandas as pd
import configparser as cp

class vec:
    def gen_billing():
        print('Start billing\n')
        
    def gen_dr_dates():
        print("Set DR dates\n")
        config = cp.ConfigParser()
        config.read("myfile.ini")
        print(config.sections())
        print(config.get('SectionThree', 'drdate'))
        return config.get('SectionThree', 'drdate')
        
    def get_baseline():
        print('baseline\n')
        
    def calc_performance():
        print('Performance')
    
    def gen_forcast():
        print('Forcasting\n')