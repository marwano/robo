#!/usr/bin/env python3
from datetime import datetime
import cv2

ESC_KEY = 27
BLUE = (255, 0, 0)
FONT = cv2.FONT_HERSHEY_SIMPLEX
TEXT_POS = (10, 30)
MSG_FRAME_COUNT = 10

def save_photo(frame):
    stamp = datetime.now().isoformat().replace(':', '.')
    cv2.imwrite(f'photo_{stamp}.jpg', frame)

def show_image(frame, messages):
    if messages:
        cv2.putText(frame, messages.pop(), TEXT_POS, FONT, 1, BLUE)
    cv2.imshow('preview', frame)

def set_message(messages, text):
    messages[:] = [text] * MSG_FRAME_COUNT

def main():
    cap = cv2.VideoCapture(0)
    assert cap.isOpened(), 'Cannot open camera'

    messages = []
    while (key := cv2.waitKey(1)) not in [ord('q'), ESC_KEY]:
        ret, frame = cap.read()
        assert ret, 'Cannot read frame from camera'
        if key == ord(' '):
            save_photo(frame)
            set_message(messages, 'saving photo...')
        show_image(frame, messages)

    cap.release()

if __name__ == "__main__":
    main()
