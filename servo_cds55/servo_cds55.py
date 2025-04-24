import time
import digitalio
import board
import busio


class ServoCds55:
    def __init__(self, cs_pin=board.D8):
        self.cs = digitalio.DigitalInOut(cs_pin)
        self.cs.direction = digitalio.Direction.OUTPUT
        self.cs.value = True  # Chip Select HIGH to start

        self.velocity_temp = 150
        self.upper_limit_temp = 300

        self.spi = busio.SPI(clock=board.SCLK, MOSI=board.MOSI, MISO=board.MISO)
        while not self.spi.try_lock():
            pass
        try:
            self.spi.configure(baudrate=2000000, phase=0, polarity=0)
        finally:
            self.spi.unlock()

    def _transfer_and_wait(self, data):
        self.spi.try_lock()
        try:
            self.spi.write(bytes([data]))
        finally:
            self.spi.unlock()
        time.sleep(0.00002)  # 20 µs delay

    def set_velocity(self, velocity):
        self.velocity_temp = velocity

    def set_pos_limit(self, pos_limit):
        self.upper_limit_temp = pos_limit

    def write(self, ID, Pos):
        self.set_servo_limit(ID, self.upper_limit_temp)
        self.write_pos(ID, Pos)

    def rotate(self, ID, velocity):
        self.set_servo_limit(ID, 0)
        time.sleep(0.1)
        self.set_motor_mode(ID, velocity)

    def write_pos(self, ID, Pos):
        posB = (Pos >> 8) & 0xFF
        posS = Pos & 0xFF
        velB = (self.velocity_temp >> 8) & 0xFF
        velS = self.velocity_temp & 0xFF
        self.cs.value = False
        for b in ["p", ID, posB, posS, velB, velS, "\t", "\r", "\n"]:
            self._transfer_and_wait(ord(b) if isinstance(b, str) else b)
        self.cs.value = True
        time.sleep(0.01)

    def set_servo_limit(self, ID, upper_limit):
        upperB = (upper_limit >> 8) & 0xFF
        upperS = upper_limit & 0xFF
        self.cs.value = False
        for b in ["s", ID, upperB, upperS, "\t", "\r", "\n"]:
            self._transfer_and_wait(ord(b) if isinstance(b, str) else b)
        self.cs.value = True
        time.sleep(0.01)

    def set_motor_mode(self, ID, velocity):
        velB = (velocity >> 8) & 0xFF
        velS = velocity & 0xFF
        self.cs.value = False
        for b in ["m", ID, velB, velS, "\t", "\r", "\n"]:
            self._transfer_and_wait(ord(b) if isinstance(b, str) else b)
        self.cs.value = True
        time.sleep(0.01)

    def set_id(self, ID, newID):
        self.cs.value = False
        for b in ["i", ID, newID, "\t", "\r", "\n"]:
            self._transfer_and_wait(ord(b) if isinstance(b, str) else b)
        self.cs.value = True
        time.sleep(0.01)

    def reset(self, ID):
        self.cs.value = False
        for b in ["r", ID, "\t", "\r", "\n"]:
            self._transfer_and_wait(ord(b) if isinstance(b, str) else b)
        self.cs.value = True
        time.sleep(0.01)
