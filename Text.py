import cv2
from datetime import datetime

def main_text(frame):
    # describe the type of font 
	# to be used. 
    font = cv2.FONT_HERSHEY_SIMPLEX
    now = datetime.now()
    
    # Format: "2025-05-03 15:24:01"
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
	# Use putText() method for 
	# inserting text on video 
    cv2.putText(frame,
                timestamp,
                (10, 30),   # X, Y position on screen
                font, 0.8,
                (0, 255, 255),  # Color (BGR): Yellow
                2,
                cv2.LINE_AA)
