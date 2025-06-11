# 🔍 Face Detection in Video

![OpenCV](https://img.shields.io/badge/OpenCV-5.3.0-green) ![Python](https://img.shields.io/badge/Python-3.8+-blue)

This Python script detects faces in a video file using OpenCV's Haar Cascade classifier.

## ✨ Features

- Real-time face detection in video frames
- Intelligent frame resizing while maintaining aspect ratio
- Optimized for large video files (4K/HD supported)
- Simple keyboard controls (press 'q' to quit)
- Clear visual feedback with bounding boxes

## ✅ Requirements

- Python 3.8+
- OpenCV (cv2) 4.5+
- NumPy

## ⚙️Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/face-detection-video.git
   cd face-detection-video
2. Install dependencies:
 ```bash
pip install opencv-python numpy
```
## 🚀 Usage

- Edit the script to specify your video path:video_path = 'path/to/your/video.mp4' 

## 🔍 Run the detection script:
```bash
python face_detection_video.py
```
## 🎮 Controls  

- 🛑 q to quit the program
- ⏯️ space to pause/resume

## 🛠️ Customization
```
# Detection parameters (in script)
scale_factor = 1.3   # 🔍 Detection sensitivity
min_neighbors = 5    # 👥 Minimum face matches
```

## ⁉️ Troubleshooting
❓ No faces detected?
✅ Adjust lighting conditions
✅ Check camera angle (frontal faces work best)
🐢 Slow performance?
✅ Reduce max_width/max_height in resize_frame()

## 📸 Output
- Detected faces shown with blue bounding boxes

![Screenshot](https://i.ibb.co/chyXNPh6/demo-screenshot.png)
