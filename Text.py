import cv2

def main_text (frame):
	# describe the type of font 
	# to be used. 
    font = cv2.FONT_HERSHEY_SIMPLEX 

	# Use putText() method for 
	# inserting text on video 
    cv2.putText(frame, 
				'TEXT ON VIDEO', 
				(50, 50), 
				font, 1, 
				(0, 255, 255), 
				2, 
				cv2.LINE_4) 

