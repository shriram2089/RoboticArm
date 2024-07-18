from machine import Pin, PWM
import time
class Servo:
    # these defaults work for the standard TowerPro SG90
    __servo_pwm_freq = 50
    __min_u10_duty = 26 - 0 # offset for correction
    __max_u10_duty = 123- 0  # offset for correction
    min_angle = 0
    max_angle = 180
    current_angle = 0.001


    def __init__(self, pin):
        self.__initialise(pin)


    def update_settings(self, servo_pwm_freq, min_u10_duty, max_u10_duty, min_angle, max_angle, pin):
        self.__servo_pwm_freq = servo_pwm_freq
        self.__min_u10_duty = min_u10_duty
        self.__max_u10_duty = max_u10_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.__initialise(pin)


    def move(self, angle):
        # round to 2 decimal places, so we have a chance of reducing unwanted servo adjustments
        angle = round(angle, 2)
        # do we need to move?
        if angle == self.current_angle:
            return
        self.current_angle = angle
        # calculate the new duty cycle and move the motor
        duty_u10 = self.__angle_to_u10_duty(angle)
        self.__motor.duty(duty_u10)

    def __angle_to_u10_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u10_duty

    def set_servo(self,angle,correction = False):
        if correction:
            angle *=190/180
            angle = int(angle)
        start = self.current_angle
        direction = (start<angle)
        for i in range(int(abs(start-angle))):
            if direction :
                self.move(start+i)
                time.sleep(0.05)
               
            else:
                self.move(start-i)
                time.sleep(0.05)
               
        self.move(angle)
        time.sleep(0.02)


    def __initialise(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (self.__max_u10_duty - self.__min_u10_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(pin))
        self.__motor.freq(self.__servo_pwm_freq)
        
  
  
PIN = 4
PIN_2 = 2
    
servo1 = Servo(PIN)
servo2 = Servo(PIN_2)

servo1.set_servo(0)
servo2.set_servo(0)

'''
if __name__ == "__main__":
    PIN = 4
    PIN_2 = 15
    
    servo1 = Servo(PIN)
    servo2 = Servo(PIN_2)
    
    angle = float(input("ENTER THE ANGLE: "))

    servo1.set_angle(angle)
'''

