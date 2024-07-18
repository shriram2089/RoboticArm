from machine import Pin, PWM
import time

# Define GPIO pin for the servo signal
SERVO_PIN_1 = 18  # Example GPIO pin for the servo signal

SERVO_PIN_2  = 20

def setup_servo(PIN):
    # Setup PWM pin
    global servo_pwm
    servo_pwm = PWM(Pin(PIN), freq=50)  # 50 Hz frequency for typical servo motors


def move_servo(angle):
    
    
if __name__ == "__main__":
    angle = float(input())
    pin = int(input())
    setup_servo(pin)
    move_servo(angle)
    
    