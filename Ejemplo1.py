import sim
import sys
import time

print('Program started')
sim.simxFinish(-1)  # just in case, close all opened connections
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Connect to CoppeliaSim
if clientID != -1:
    print('Connected to remote API server')
    # Guardar la referencia de los motores
    _, left_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', sim.simx_opmode_oneshot_wait)
    _, right_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', sim.simx_opmode_oneshot_wait)

    velocidad = 0.65  # Variable para la velocidad de los motores
    sim.simxSetJointTargetVelocity(clientID, left_motor_handle, velocidad, sim.simx_opmode_streaming)
    sim.simxSetJointTargetVelocity(clientID, right_motor_handle, velocidad, sim.simx_opmode_streaming)
    time.sleep(5)
    sim.simxSetJointTargetVelocity(clientID, left_motor_handle, -velocidad, sim.simx_opmode_streaming)
    sim.simxSetJointTargetVelocity(clientID, right_motor_handle,velocidad, sim.simx_opmode_streaming)
    time.sleep(1)
    sim.simxSetJointTargetVelocity(clientID, left_motor_handle, velocidad, sim.simx_opmode_streaming)
    sim.simxSetJointTargetVelocity(clientID, right_motor_handle, velocidad, sim.simx_opmode_streaming)
    time.sleep(5)
    sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 0, sim.simx_opmode_streaming)
    sim.simxSetJointTargetVelocity(clientID, right_motor_handle,0, sim.simx_opmode_streaming)
    time.sleep(1)
    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
else:
    sys.exit('Failed connecting to remote API server')
print('Program ended')
