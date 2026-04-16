# Arduino Nano + IMU (BNO055) Setup with Raspberry Pi

## 📌 Overview
This project demonstrates how to interface a **BNO055 IMU sensor** with an **Arduino Nano** and stream orientation data to a **Raspberry Pi (or Ubuntu system)** using serial communication.

Pipeline:
BNO055 (I2C) → Arduino Nano → USB Serial → Raspberry Pi → Python


---

## 🔧 Hardware Requirements
- Arduino Nano (ATmega328P)
- BNO055 IMU sensor
- Breadboard
- Jumper wires
- USB cable (data cable)

---

## 🔌 Wiring Connections

| Arduino Nano | BNO055 |
|-------------|--------|
| 5V          | VIN    |
| GND         | GND    |
| A5          | SCL    |
| A4          | SDA    |

---

## 💻 Arduino Setup (Ubuntu / Raspberry Pi)

### 1. Install Arduino IDE (Recommended)

```bash
cd ~/Downloads
wget https://downloads.arduino.cc/arduino-ide/arduino-ide_latest_Linux_64bit.AppImage
chmod +x arduino-ide_latest_Linux_64bit.AppImage
./arduino-ide_latest_Linux_64bit.AppImage
```
### 2. Configure Arduino IDE
Board: Arduino Nano
Processor: ATmega328P (try Old Bootloader if upload fails)
Port: /dev/ttyUSB0


### 3. Install Required Libraries
Sketch → Include Library → Manage Libraries

Install:

Adafruit BNO055
Adafruit Unified Sensor

### 4. Run the "imudatastreaming_arduino.cpp" code in arduino and check output in serial monitor
Expected output:
359.93,4.50,5.43

### 5. Raspi setup

```bash 
pip3 install pyserial
```
Use the scripts in src/utils/imudatareader.py to test the communication of raspi with arduino

Note: The Arduino Nano should be powered using the blue cable connected to Raspi USB port this will enable the serial communication.

👨‍💻 Author

Rahul Ravi VK
Robotics | Controls | Perception