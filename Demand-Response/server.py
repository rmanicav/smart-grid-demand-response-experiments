import asyncio
from datetime import datetime, timezone, timedelta
from openleadr import OpenADRServer, enable_default_logging
from functools import partial
import logging
from vectn.vecclass import vec as vc
from utilities.connect import connectclass as c


enable_default_logging()

async def insert_customer(custData):
             
    con=c.connect()
    # create a database connection
    conn = con.create_connection()
    con.insert_customer(conn,custdata)

async def update_customer(custData):
             
    con=c.connect()
    # create a database connection
    
    conn = con.create_connection()
    con.update_customer(conn,custdata)
    
async def insert_meter(meterData):
               
    conn=c.connect()
    # create a database connection
    conn = conn.create_connection()
    conn.insert_meter(conn,meterData)     
    
async def update_meter(meterData):
               
    conn=c.connect()
    # create a database connection
    conn = conn.create_connection()
    conn.update_meter(conn,meterData)          
    
async def gen_report():
          
    con=c.connect()
    # create a database connection
    conn = con.create_connection()
    conn.gen_report(conn)  
    

async def on_create_party_registration(registration_info):
    """
    Inspect the registration info and return a ven_id and registration_id.
    """
    vc.gen_dr_dates()
    if registration_info['ven_name'] == 'ven123':
        ven_id = 'ven_id_123'
        registration_id = 'reg_id_123'
        return ven_id, registration_id
    else:
        return False


async def on_register_report(ven_id, resource_id, measurement, unit, scale,
                             min_sampling_interval, max_sampling_interval):
    """
    Inspect a report offering from the VEN and return a callback and sampling interval for receiving the reports.
    """
    success =insert_meter(measurement)

    callback = partial(on_update_report, ven_id=ven_id,
                       resource_id=resource_id, measurement=measurement)
    sampling_interval = min_sampling_interval
    return callback, sampling_interval


async def on_update_report(data, ven_id, resource_id, measurement):
    """
    Callback that receives report data from the VEN and handles it.
    """
    print("Measurement is \t:", data[0][1])
    high = util.getMsrlimit()
    print("\nUpper Limit is \t:", high)
    if (data[0][1] > high):
        print("Exceeded the limit of voltage 10")
    else:
        for time, value in data:
            print(
                f"Ven {ven_id} reported {measurement} = {value} at time {time} for resource {resource_id}")


async def event_response_callback(ven_id, event_id, opt_type):
    """
    Callback that receives the response from a VEN to an Event.
    """
    print(f"VEN {ven_id} responded to Event {event_id} with: {opt_type}")

# Create the server object
server = OpenADRServer(vtn_id='myvtn')

# Add the handler for client (VEN) registrations
server.add_handler('on_create_party_registration',
                   on_create_party_registration)

# Add the handler for report registrations from the VEN
server.add_handler('on_register_report', on_register_report)





# Add a prepared event for a VEN that will be picked up when it polls for new messages.
server.add_event(ven_id='ven_id_123',
                 signal_name='simple',
                 signal_type='level',
                 intervals=[{'dtstart': datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
                             'duration': timedelta(minutes=10),
                             'signal_payload': 1}],
                 callback=event_response_callback)

# Run the server on the asyncio event loop
loop = asyncio.get_event_loop()
loop.create_task(server.run())
loop.run_forever()
