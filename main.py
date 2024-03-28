import cv2
from ultralytics import YOLO
import time

# Initialize YOLO model
yolo = YOLO("yolo-Weights/yolov5s.pt")

# Initialize webcam
# cap = cv2.VideoCapture(0) 



# Load video file
video_path = "real_time.mp4"
cap = cv2.VideoCapture(video_path)

# Set resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Variables to store previous ball positions
prev_ball_centers = []

while True:
    # Capture frame from video
    ret, frame = cap.read()
    if not ret:
        break

    # Use YOLO to detect objects in the frame
    results = yolo(frame)
    for r in results:
        boxes = r.boxes
        for obj in boxes:
            # Extract object coordinates and class
            x1, y1, x2, y2 = obj.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cls = int(obj.cls[0])
            class_name = yolo.names[int(cls)]
            if class_name == "sports ball":
                # Calculate the center of the ball
                ball_center = ((x1 + x2) // 2, (y1 + y2) // 2)
                
                # Draw a bounding box around the detected object
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                # Display class name and confidence
                cv2.putText(frame, f"{class_name}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                # Store the current ball position
                prev_ball_centers.append(ball_center)
                
                # Draw trajectory based on previous ball positions
                for i in range(1, len(prev_ball_centers)):
                    cv2.line(frame, prev_ball_centers[i - 1], prev_ball_centers[i], (0, 0, 255), 2)
                
                # Calculate speed if previous positions are available
                if len(prev_ball_centers) > 1:
                    # Calculate distance between consecutive positions
                    distance = cv2.norm(prev_ball_centers[-1], prev_ball_centers[-2])
                    
                    # Calculate time difference between frames
                    time_diff = time.perf_counter() - start_time
                    
                    # Calculate speed (distance / time)
                    if time_diff > 0:
                        speed = distance / time_diff
                        cv2.putText(frame, f"Speed: {speed:.2f} pixels per second", (x1, y1 - 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                        
                # Update start time for next frame
                start_time = time.perf_counter()

    # Display the frame
    cv2.namedWindow('Object Detection', cv2.WINDOW_NORMAL)
    cv2.imshow('Object Detection', frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
