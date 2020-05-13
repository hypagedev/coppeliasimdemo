import sim
import sys

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connected to remote API server')

   
    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
else:
    sys.exit('Failed connecting to remote API server')
print ('Program ended')
