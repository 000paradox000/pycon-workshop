import os
import time
import uuid

import cv2

BASE_FOLDER = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
VIDEOS_FOLDER = f"{BASE_FOLDER}/videos"
FRAMES_FOLDER = f"{BASE_FOLDER}/frames"
ESCAPE_KEY = 27
CAMERA_INDEX = 0

first_name = "Ariel"
last_name = "Calzada"

HOME_FOLDER_VIDEOS = f"{VIDEOS_FOLDER}/{first_name.upper()}__{last_name.upper()}"
HOME_FOLDER_FRAMES = f"{FRAMES_FOLDER}/{first_name.upper()}__{last_name.upper()}"

if not os.path.exists(HOME_FOLDER_VIDEOS):
  os.makedirs(HOME_FOLDER_VIDEOS)

if not os.path.exists(HOME_FOLDER_FRAMES):
  os.makedirs(HOME_FOLDER_FRAMES)

video_path = f"{HOME_FOLDER_VIDEOS}/ariel.avi"
cap = cv2.VideoCapture(CAMERA_INDEX)
video_length = 5  # seconds

start_time = time.clock()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_video = cv2.VideoWriter(video_path, fourcc, 20.0, (640,480))
seconds = 0

while time.clock() - start_time <= video_length:
    # Get a frame
    ret, frame = cap.read()

    # Save frame
    frame_name = f"{uuid.uuid4().hex}.jpg"
    frame_path = f"{HOME_FOLDER_FRAMES}/{frame_name}"
    cv2.imwrite(frame_path, frame)

    # Update video video
    out_video.write(frame)

    # Show the frame
    cv2.imshow("frame", frame)

    # Wait a second for user to press any KEY
    pressed_key = cv2.waitKey(1) & 0xFF

    if pressed_key == ESCAPE_KEY:
      break

cap.release()
out_video.release()
cv2.destroyAllWindows()