import time
import socket
from dronekit import connect
import threading
import signal

connection_string = 'udp:127.0.0.1:14553'

print("Connecting to vehicle on: %s" % (connection_string,))
try:
    vehicle = connect(connection_string, wait_ready=True)
except socket.error as e:
    print(e)
    # proceed just with a blank object so I can render the tree
    vehicle=None

while vehicle.commands.next <  12:

    # 20m @ TWENTI WP 5
    if vehicle.commands.next == 5:
        vehicle.parameters['RNGFND2_SCALING']=4

    # 10m @ TENNA WP 7
    if vehicle.commands.next == 7:
        vehicle.parameters['RNGFND2_SCALING']=2

    # 5m @ ALPHA WP 9
    if vehicle.commands.next == 9:
        vehicle.parameters['RNGFND2_SCALING']=1

    # 50m for the remainder of the mission
    if vehicle.commands.next > 9:
        vehicle.parameters['RNGFND2_SCALING']=10
    
    time.sleep(0.5)

vehicle.close()