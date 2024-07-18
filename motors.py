from inverse import inverse_kinematics
from stepper_final import Stepper_motor
from servo_2 import Servo

import time

SERVO_1 = 4
SERVO_2 =2
servo1 = Servo(SERVO_1)
servo2 = Servo(SERVO_2)

stepper = Stepper_motor()

def stepperControl(t1):
    #t1,t2,t3 = inverse_kinematics(x,y,z)
    stepper.set_stepper(t1)
    
    
def shoulder(t2):
    
    
    servo1.set_servo(t2)
    

def elbow(t3):
    
    servo2.set_servo(t3)
    
def wait_until_stepper_stops():
    time.sleep(3)

def wait_until_servo_stops():
    time.sleep(3)

def main():
    
    while 1:
            target_x = float(input("Enter target x-coordinate: "))
            target_y = float(input("Enter target y-coordinate: "))
            target_z = float(input("Enter target z-coordinate: "))
            
            if(target_z<8):
                return None
            
            t1,t2,t3 = inverse_kinematics(target_x, target_y, target_z)
            print(t1,t2,t3)
            
            
            stepperControl(t1)
            #wait_until_stepper_stops()
            shoulder(t2)
            #wait_until_servo_stops()
            elbow(t3)
            


def actuate(t1,t2,t3):
    set_stepper(t1)
    servo1.set_servo(t2)
    servo2.set_servo(t3)
  
if __name__ == "__main__":
     main()
