# AUTONOMOUS-ROBOT-BUILD-SERIES
 
A hands-on robotics project exploring computer vision techniques for autonomous navigation — from basic color detection to real-time object tracking on a Raspberry Pi.
 
> **🚧 This project is actively under development.** New modules, demos, and documentation are being added regularly. Star or watch the repo to stay updated!
 
---
 
## Project Structure
 
```
AUTONOMOUS-ROBOT-BUILD-SERIES/
│
├── assets/images/                  # Input images for processing
│   └── traffic_light.jpg
│
├── data log/contour detection/     # Logged data
│   └── recording_data.txt
│
├── results/                        # Output from processing pipeline
│   └── contour detection/
│       ├── images/                 
│       │   ├── contour_id.png
│       │   └── hsv_pipeline.png
│       ├── performance analysis/
│       │   └── Figure_1.png
│       └── videos/                 
│           ├── contour_detection_video_hw3.mp4
│           └── traffic_light_detection.mp4
│
├── src/vision/
│   ├── contour detection/          # Core vision modules
│   │   ├── contour_detection.py
│   │   ├── hsv_masking.py
│   │   ├── object_tracking.py
│   │   ├── performance_logging.py
│   │   ├── performance_plotting.py
│   │   └── video_creator_from_frames.py
│   └── utils/                      # Hardware utilities
│       ├── picam2_image_capture_test.py
│       └── picam2_video_capture_test.py
│
└── README.md
```
 
---
