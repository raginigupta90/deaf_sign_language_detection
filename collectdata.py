import os
import cv2

def create_directories(base_dir):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        dir_path = os.path.join(base_dir, letter)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

# Set up the video capture
cap = cv2.VideoCapture(0)
directory = 'Image/'

# Create directories for each letter
create_directories(directory)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break
    
    count = {letter.lower(): len(os.listdir(os.path.join(directory, letter))) for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    
    # Draw rectangle and display frames
    cv2.rectangle(frame, (0, 40), (300, 400), (255, 255, 255), 2)
    cv2.imshow("data", frame)
    roi = frame[40:400, 0:300]
    cv2.imshow("ROI", roi)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF in range(ord('a'), ord('z') + 1):
        char = chr(interrupt & 0xFF)
        cv2.imwrite(os.path.join(directory, char.upper(), f'{count[char]}.png'), roi)
    
    if interrupt & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
