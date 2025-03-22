import cv2  # OpenCV for video capture

cap = cv2.VideoCapture(0)  # Open the default camera

while True:
    success, frame = cap.read()  # Read a frame from the camera
    if not success:
        break  # If frame is not captured correctly, exit loop

    cv2.imshow("Camera Feed", frame)  # Show the camera feed

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()  # Close all OpenCV windows
