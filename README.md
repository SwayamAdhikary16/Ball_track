# Ball Tracker with YOLO

This project utilizes the YOLO (You Only Look Once) object detection algorithm to track a ball in a video feed or webcam stream. It draws a bounding box around the detected ball, tracks its trajectory, and calculates its speed.

## Requirements

- Python 3.x
- OpenCV
- Ultralytics YOLO
- A video file or webcam

## Installation

1. Clone this repository:
   
git clone https://github.com/SwayamAdhikary16/Ball_track.git

3. Install the required packages:

pip install opencv-python-headless
pip install yolov5 # or any YOLO version


3. Place your YOLO weights file (`yolov5s.pt` or similar) in the `yolo-Weights` folder.

## Usage

1. Place your video file (e.g., `real_time.mp4`) in the project directory.

2. Run the script:


3. Press 'q' to exit the program.

## Configuration

- You can modify the video path in the script to use your own video file.

- You can adjust the resolution of the video feed by modifying the `set` methods on the `cap` object.




     
