import machine
import time

class TMC2208:

    # Initialize the TMC2208 driver with the given UART parameters and pin assignments
    def __init__(self, uart_num, baudrate, rx_pin, tx_pin, en_pin, dir_pin, step_pin):
        self.uart = machine.UART(uart_num, baudrate=baudrate, rx=rx_pin, tx=tx_pin)
        self.en_pin = machine.Pin(en_pin, machine.Pin.OUT)
        self.dir_pin = machine.Pin(dir_pin, machine.Pin.OUT)
        self.step_pin = machine.Pin(step_pin, machine.Pin.OUT)
        
        # Set the driver enable pin high to enable the driver
        self.en_pin.value(1)

    # Send a command to the TMC2208 driver over UART
    def send_command(self, cmd):
        self.uart.write(cmd + b'\n')
        response = self.uart.readline()
        return response

    # Set the microstep mode of the driver
    def set_microstep_mode(self, mode):
        cmd = 'V{}'.format(mode).encode()
        self.send_command(cmd)

    # Set the direction of the motor
    def set_direction(self, direction):
        self.dir_pin.value(direction)

    # Step the motor the given number of steps at the given speed
    def step(self, steps, delay_us):
        for i in range(steps):
            self.step_pin.value(1)
            time.sleep_us(delay_us)
            self.step_pin.value(0)
            time.sleep_us(delay_us)

    # Disable the driver
    def disable_driver(self):
        self.en_pin.value(1)
        
    def enable_driver(self):
    	self.en_pin.value(0)
