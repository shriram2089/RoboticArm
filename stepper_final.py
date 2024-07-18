import machine
import time
from tmc2208 import TMC2208

class Stepper_motor:
    
    
    
    def __init__(self,en_pin = 14, dir_pin = 13, step_pin = 12):
            
        self.previous_angle = 0
        self.a = 0


            # Create an instance of the TMC2208 driver with the appropriate UART parameters and pin assignments
        self.tmc2208 = TMC2208(uart_num=2, baudrate=115200, rx_pin=16, tx_pin=17, en_pin=en_pin , dir_pin=dir_pin, step_pin=step_pin)

            # Set the microstep mode to 1/16 step
        self.tmc2208.set_microstep_mode(4)

            # Set the number of steps for a full rotation (in this case, 200 steps per revolution for a 1.8 degree/step motor)
        self.steps_per_revolution = 200

            # Set the delay between steps (in microseconds)
        self.delay_us = 500

            # Set the direction to clockwise
        self.tmc2208.set_direction(1)
        self.tmc2208.enable_driver()
            # Step the motor 200 steps for a full rotation, so 360 degrees requires 200*360/360=200 steps
        
   
    def  move_stepper(self,angle):
         
        self.a = angle - self.previous_angle
        steps = int((abs(self.a)*1600)/360)
        print(self.a,steps)
        if self.a<0 :
            self.tmc2208.set_direction(1)
            self.tmc2208.step(steps,self.delay_us)
           
        else :
            self.tmc2208.set_direction(0)
            self.tmc2208.step(steps,self.delay_us)
           
        self.previous_angle = angle
        
    def set_stepper(self,angle,correction = False):
            if correction:
                angle *=190/180
                angle = int(angle)
            start = self.previous_angle
            direction = (start<angle)
            for i in range(int(abs(start-angle))):
                if direction :
                    self.move_stepper(start+i)
                    time.sleep(0.04)
                   
                else:
                    self.move_stepper(start-i)
                    time.sleep(0.04)
                   
            self.move_stepper(angle)
            time.sleep(0.04)
            
step = Stepper_motor()

        
#if __name__ == "__main__":
    
#angle = float(input("Enter Angle: "))



