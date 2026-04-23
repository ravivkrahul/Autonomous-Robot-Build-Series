# Autonomous Robot Build Series

An end-to-end autonomous robot project covering computer vision (contour detection, arrow detection, traffic-light detection), localization (wheel encoders + IMU fusion), hardware testing utilities, and performance analysis. Built around a Raspberry Pi + PiCam2 + Arduino Nano (BNO055 IMU) stack.

---

## 📁 Folder Structure

```
AUTONOMOUS-ROBOT-BUILD-SERIES/
│
├── assets/
│   └── images/                              # Input images for vision pipelines
│       ├── all_objects.jpg
│       ├── arrow.JPG
│       ├── blue.jpg
│       ├── green.jpg
│       ├── red.jpg
│       └── traffic_light.jpg
│
├── data log/                                # Logged runtime data
│   ├── arrow detection/
│   │   └── hw4_recording_data.txt
│   ├── contour detection/
│   │   └── recording_data.txt
│   └── encoder vs encoder+imu/
│       ├── encoder_imu_rectangle.csv
│       └── encoder_only_rectangle.csv
│
├── datasheets/                              # Hardware reference documents
│   ├── Arduino-nano-pinout.png
│   ├── GPIOconfig.png
│   ├── HCSR04.pdf
│   ├── L298n.pdf
│   ├── Proton Servo (Steel Gears, 180°).pdf
│   ├── ROB0025-Instruction Manual.pdf
│   ├── RP-008156-DS-2-picamera2-datasheet.pdf
│   ├── RP-008341-DS-1-raspberry-pi.pdf
│   ├── adafruit-bno055-absolute-orientation-sensor.pdf
│   └── bst-bno055-ds000.pdf
│
├── demos/                                   # Demonstration videos
│   ├── contour_detection.mp4
│   ├── encoder_count_test.mp4
│   ├── encoder_vs_encoder+imu.mp4
│   ├── first_run.mp4
│   ├── gripper_operation.mp4
│   └── teleop_with_ultrasonic.mp4
│
├── results/                                 # Output from processing pipelines
│   ├── arrow detection/
│   │   └── performance/
│   │       └── plot1.png
│   ├── contour detection/
│   │   ├── images/
│   │   │   ├── contour_id.png
│   │   │   └── hsv_pipeline.png
│   │   ├── performance analysis/
│   │   │   └── Figure_1.png
│   │   └── videos/
│   │       ├── contour_detection_video_hw3.mp4
│   │       └── traffic_light_detection.mp4
│   └── encoder vs encoder+imu/
│       ├── encoder_only.png
│       └── imu_encoder.png
│
├── src/                                     # Source code
│   ├── Arduino_nano/
│   │   ├── imudatastreaming_arduino.cpp     # IMU data streaming firmware
│   │   └── readme.md
│   │
│   ├── localization/
│   │   └── encoder vs encoder+imu/
│   │       ├── encoder.py                   # Encoder-only odometry
│   │       ├── plotter.py                   # Plotting helper
│   │       └── imuencoder.py                # Fused encoder + IMU odometry
│   │
│   ├── utils/                               # Hardware test & helper utilities
│   │   ├── colorpicker.py
│   │   ├── encoderdebug.py
│   │   ├── gripper_test_tune.py
│   │   ├── imu_x.py
│   │   ├── imudatareader.py
│   │   ├── picam2_image_capture_test.py
│   │   ├── picam2_video_capture_test.py
│   │   ├── qrcode_reader.py
│   │   └── ultrasonic_test.py
│   │
│   └── vision/                              # Computer vision modules
│       ├── arrow_detection/
│       │   ├── arrow_detection_image.py
│       │   └── arrow_detection_video.py
│       ├── color hsv picker/
│       │   └── colorpicker.py
│       └── contour_detection/
│           ├── contour_detection.py
│           ├── hsv_masking.py
│           ├── object_tracking.py
│           ├── performance_logging.py
│           ├── performance_plotting.py
│           └── video_creator_from_frames.py
│
├── .gitignore
├── Arena_layout_and_QR_Codes.pdf            # Arena layout & QR code reference
├── setup.sh
└── README.md
```

---

## 📂 Directory Overview

### `assets/images/`
Static input images used by the vision pipelines for testing detection, color masking, and identification (traffic lights, arrows, colored objects).

### `data log/`
Runtime logs captured during experiments, organized by sub-task:
- **arrow detection** — raw recordings from arrow-tracking runs
- **contour detection** — frame/timing logs from contour-tracking runs
- **encoder vs encoder+imu** — CSV traces of a rectangular path run with encoder-only vs. fused encoder+IMU odometry

### `datasheets/`
Reference PDFs and pinout diagrams for every hardware component in the build: Raspberry Pi, PiCam2, Arduino Nano, BNO055 IMU, HC-SR04 ultrasonic sensor, L298N motor driver, Proton servo, and ROB0025.

### `demos/`
Short MP4 clips showcasing working subsystems — first run, gripper operation, teleop with ultrasonic obstacle avoidance, encoder counting, and the encoder vs. encoder+IMU comparison.

### `results/`
Generated outputs organized by experiment: annotated images, performance plots, and rendered videos from the detection and localization pipelines.

### `src/`
All source code, split by domain:
- **Arduino_nano/** — firmware running on the Nano (IMU streaming over serial)
- **localization/** — Python odometry scripts comparing encoder-only vs. fused encoder+IMU pose estimation
- **utils/** — standalone hardware sanity-check scripts (camera capture, QR reading, ultrasonic test, IMU reader, encoder debug, gripper tuning, etc.)
- **vision/** — the main perception stack: arrow detection, HSV color picker, and the full contour-detection pipeline with HSV masking, object tracking, performance logging, and plotting

### Root files
- **Arena_layout_and_QR_Codes.pdf** — physical arena map and QR code reference used for navigation tasks
- **.gitignore** — standard Python/IDE ignores

---

## 🚀 Getting Started

### One-shot setup
 
A single `setup.sh` script installs every system package, creates a Python virtual environment, installs all pip dependencies, and enables the required interfaces (I2C, SSH, VNC).
 
```bash
git clone https://github.com/ravivkrahul/Autonomous-Robot-Build-Series
cd AUTONOMOUS-ROBOT-BUILD-SERIES
chmod +x setup.sh
./setup.sh
```

### Run the contour detection pipeline
```bash
cd src/vision/contour_detection
python contour_detection.py
```

### Run the encoder + IMU localization comparison
```bash
cd "src/localization/encoder vs encoder+imu"
python imuencoder.py
```

### Flash the Arduino IMU firmware
Open `src/Arduino_nano/imudatastreaming_arduino.cpp` in the Arduino IDE (or PlatformIO) and upload to the Nano connected to the BNO055.

---

## 🛠 Hardware

| Component | Purpose |
|---|---|
| Raspberry Pi | Main compute |
| PiCamera 2 | Vision input |
| Arduino Nano | IMU streaming & low-level I/O |
| BNO055 | 9-DOF orientation sensor |
| L298N | Motor driver |
| HC-SR04 | Ultrasonic distance sensor |
| Proton Servo (180°) | Gripper actuation |
| Wheel encoders | Odometry |

See `datasheets/` for the full reference set.

---

## 📊 Notable Results

- **Contour detection** — See `results/contour detection/` for HSV pipeline visualization, contour ID output, and the full detection video.
- **Encoder vs. Encoder + IMU** — See `results/encoder vs encoder+imu/` for the trajectory comparison plots on a rectangular path. Fusing IMU yaw with wheel encoders noticeably reduces heading drift.
- **Arrow detection** — Performance plot in `results/arrow detection/performance/`.

