import asyncio
from datetime import timedelta
from openleadr import OpenADRClient, enable_default_logging
import random
import sys
from meters.meter import meterclass as m
from vectn.vecgen import vecgenclass as vgen
enable_default_logging()

async def collect_report_value():
    # This callback is called when you need to collect a value for your Report
    msr =[]
    mtr = m()
    msr = mtr.meterRead()     
    print("*****************************************************************")
    print(msr)
    print("*****************************************************************")
    return msr

async def read_tcp_pkt():
    msr = random.uniform(1.0, 10.5)
    return msr

async def read_modbus_pkt():
    msr = random.uniform(1.0, 10.5)
    return msr

async def handle_event(event):
    # This callback receives an Event dict.
    # You should include code here that sends control signals to your resources.
    # Check if we can opt in to this event
    first_signal = event['event_signals'][0]
    intervals = first_signal['intervals']
    target = event['target']
    print("Event is: ", event)
    print("\n Signal name is : ", first_signal)
    return 'optIn'


# Create the client object
client = OpenADRClient(ven_name='ven123',
                       vtn_url='http://localhost:8080/OpenADR2/Simple/2.0b')

# Add the report capability to the client
client.add_report(callback=collect_report_value,
                  resource_id='device001',
                  measurement='voltage',
                  sampling_rate=timedelta(seconds=5))


# Add event handling capability to the client
client.add_handler('on_event', handle_event)

# Run the client in the Python AsyncIO Event Loop
loop = asyncio.get_event_loop()
loop.create_task(client.run())
loop.run_forever()


