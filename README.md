# dfRobot Dynamixel SPI with Python

This is a Python library for controlling DFRobot's Dynamixel motors using SPI communication.

## Requirements

- Raspberry Pi 4B or 5B
- Python 3.7 or higher
- [DFROBOT Digital Servo Shield for Dynamixel AX](https://www.dfrobot.com/product-958.html)
- [Dynamixel AX-12A](https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/)
- 12V power supply

## Wiring

| Pin Type    | DFROBOT servo driver | Raspberry Pi 4 or 5B |
| ----------- | -------------------- | -------------------- |
| VCC (POWER) | VCC                  | N/A                  |
| GND (POWER) | GND                  | N/A                  |
| 5V          | 5V                   | 5V                   |
| GND         | GND                  | GND                  |
| SCK         | GPIO13               | GPIO11               |
| MISO        | GPIO12               | GPIO9                |
| MOSI        | GPIO11               | GPIO10               |
| CS          | GPIO8                | GPIO8                |

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
3. Activate I2C, SPI, Serial and Camera interfaces:
   ```bash
   sudo raspi-config nonint do_i2c 0
   sudo raspi-config nonint do_spi 0
   sudo raspi-config nonint do_serial_hw 0
   sudo raspi-config nonint do_ssh 0
   sudo raspi-config nonint do_camera 0
   sudo raspi-config nonint disable_raspi_config_at_boot 0
   ```
4. Enable dtoverlay for spi0-0cs
   ```bash
   sudo nano /boot/firmware/config.txt
   ```
   Add the following line at the end of the file:
   ```
   dtoverlay=spi0-0cs
   ```
5. Reboot the Raspberry Pi:

   ```bash
    sudo reboot
   ```

6. Activate the virtual environment again:

   ```bash
   source venv/bin/activate
   ```

7. Install Adafruit Blinka:
   ```bash
   sudo apt-get install -y i2c-tools libgpiod-dev python3-libgpiod
   pip install --upgrade pip
   pip install --upgrade RPi.GPIO
   pip install --upgrade adafruit-blinka
   ```
8. (Optional for RPI5) Delete rpi.gpio and install rpi-lpgpio:

   ```bash
   sudo apt remove -y python3-rpi.gpio
   pip uninstall -y RPi.GPIO
   pip install --upgrade rpi-lgpio
   ```

9. Execute `servo_test.py` to test the servo:
   ```bash
   python3 servo_test.py
   ```
