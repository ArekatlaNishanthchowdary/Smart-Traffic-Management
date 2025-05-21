# Smart Traffic Management System

This project uses YOLOv8 for vehicle detection and tracking to implement an intelligent traffic management system. The system can detect various types of vehicles including emergency vehicles and adjust traffic signals accordingly.

## Features

- Real-time vehicle detection using YOLOv8
- Vehicle tracking across video frames
- Emergency vehicle detection
- Traffic signal control based on traffic volume and emergency vehicles
- Traffic flow analytics

## Files

- `main.py`: Core application for vehicle detection and traffic management
- `tracker.py`: Vehicle tracking implementation
- `disp.py`: Display utilities

### Large Files (Not included in repository)

Due to GitHub file size limitations, the following files are not included in this repository:

- YOLOv8 models (yolov8x.pt, yolov8s.pt, best.pt) - Download from [Ultralytics](https://github.com/ultralytics/ultralytics)
- Video files for testing

## Requirements

- Python 3.7+
- OpenCV
- Ultralytics YOLOv8
- Pandas
- NumPy

## Installation

1. Clone this repository
2. Install dependencies: `pip install opencv-python ultralytics pandas numpy`
3. Download the required YOLOv8 model files

## Usage

Run the main script with:

```bash
python main.py
```

Press 'q' to exit the application. 