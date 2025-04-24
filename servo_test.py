"""
AX12A Servo Test
This script tests the functionality of the ServoCds55 class.

Connections:
Pin type | dfrobot servo driver | Raspberry Pi 4 or 5
SCK      | GPIO 13              | GPIO 11
MOSI     | GPIO 12              | GPIO 10
MISO     | GPIO 11              | GPIO 9
CS       | GPIO 8               | GPIO 8
GND      | GND                  | GND
VCC      | 5V                   | 5V

Available functions:
- set_velocity(velocity): Set the velocity for the servo.
- set_pos_limit(pos_limit): Set the position limit for the servo.
- write(ID, Pos): Write the specified position to the servo with the given ID.
- rotate(ID, velocity): Rotate the servo with the specified ID at the given velocity.
- write_pos(ID, Pos): Write the specified position to the servo with the given ID.
- set_servo_limit(ID, upper_limit): Set the upper limit for the servo with the specified ID.
- set_motor_mode(ID, velocity): Set the motor mode for the servo with the specified ID.
- set_id(ID, newID): Set a new ID for the servo.
- reset(ID): Reset the servo with the specified ID.

"""

from servo_cds55 import ServoCds55
import board
import time

servo = ServoCds55(
    cs_pin=board.D8
)  # Initialize the servo driver with the CS pin connected to GPIO 8
servo.rotate(1, 150)  # Rotate servo with ID 1 at velocity 150
time.sleep(2)  # Wait for 2 seconds
servo.rotate(1, -150)  # Rotate servo with ID 1 at velocity -150
time.sleep(2)  # Wait for 2 seconds
servo.rotate(1, 0)  # Stop the servo with ID 1
servo.reset(1)  # Reset the servo with ID 1
