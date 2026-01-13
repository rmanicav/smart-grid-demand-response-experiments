#Program to read configuration file for measurement limit

import configparser as cp
config = cp.ConfigParser()
config.read("myfile.ini")
print(config.sections())
print(config.options('SectionOne'))
print(config.get('SectionOne', 'vltlow'))
