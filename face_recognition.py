import cv2
import numpy as np

def resize_frame(frame, max_width=1280, max_height=720):
    """Resize frame to fit within specified dimensions while maintaining aspect ratio"""
    height, width = frame.shape[:2]
    
    # Calculate scaling factor
    scale = min(max_width/width, max_height/height)
    
    # Only resize if needed
    if scale < 1:
        return cv2.resize(frame, (int(width*scale), int(height*scale)))
    return frame

# Load pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Specify the path to your video file
video_path = r'C:\Users\Lingala Anusha\Downloads\13705569_3840_2160_25fps.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}")
else:
    # Create a resizable window
    cv2.namedWindow("Detected Faces", cv2.WINDOW_NORMAL)
    
    while True:
        ret, frame = cap.read()
        if not ret:  # End of video
            print("End of video.")
            break
        
        # Resize the frame to fit your screen
        frame = resize_frame(frame, max_width=1280, max_height=720)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Detected Faces", frame)

        # Check if 'q' is pressed to stop the video manually
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Video stopped by user.")
            break

    # Release resources and close windows after breaking out of the loop
    cap.release()
    cv2.destroyAllWindows()
    print("Face detection complete.")
