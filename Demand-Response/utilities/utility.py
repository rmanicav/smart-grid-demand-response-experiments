
import random
import configparser as cp


class util:
    # valid random measurements


    def genvalidrnd():
        # Random float number between range 1.5 to 8.5
        msr = round(random.uniform(1.5, 8.5), 2)
        return msr


# invalid random measurements
    def genvinalidrnd():
    # Random float number
        msr = print(random.uniform(15.5, 10.5))
# Output 27.23469913175497
        return msr

# get voltage limit


    def getMsrlimit():
        config = cp.ConfigParser()
        config.read("C:\\Users\\rmanicava42\\Documents\\Projects\\OpenAdr\\myfile.ini")
        # print(config.sections())
        # print(config.options('SectionOne'))
        msr = float(config.get('SectionOne', 'vlthigh'))
        return msr


    def genEthTCPPkt():
        return 1
