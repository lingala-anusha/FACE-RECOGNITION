# Face Detection in Video

This Python script detects faces in a video file using OpenCV's Haar Cascade classifier.

## Features

- Detects faces in video frames in real-time
- Maintains aspect ratio while resizing frames for display
- Handles large video files by resizing for optimal viewing
- Simple keyboard control (press 'q' to quit)

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy

## Installation

1. Install the required packages:
   ```bash
   pip install opencv-python numpy

Download the Haar Cascade XML file (included with OpenCV):

The script automatically uses the default frontal face detector included with OpenCV

## Usage
Update the video_path variable in the script to point to your video file

## Run the script:
```bash
python face_detection_video.py
Controls
Press 'q' to quit the video playback at any time

## Customization
You can adjust these parameters in the code:

max_width and max_height in resize_frame() function

Face detection parameters in detectMultiScale() (currently 1.3 scale factor and 5 minimum neighbors)

## Notes
The script will automatically exit when the video ends

For better performance on HD videos, you might need to adjust the resize parameters

The Haar Cascade classifier works best with frontal faces in good lighting conditions

## Output
The script displays the video with detected faces marked by blue rectangles.

![Screenshot 2025-06-05 195502](https://github.com/user-attachments/assets/756f70c6-4b49-4419-b81f-3e4db9587e4f)
