import cv2

BLUE = (255, 0, 0)
CV2_DIR = cv2.__path__[0]
CLASSIFIER_PATH = f'{CV2_DIR}/data/haarcascade_frontalface_default.xml'
face_classifier = cv2.CascadeClassifier(CLASSIFIER_PATH)
DETECT_SCALE = 0.2

def resize(img, scale):
    size = (int(img.shape[1] * scale), int(img.shape[0] * scale))
    return cv2.resize(img, size, interpolation=cv2.INTER_AREA)

def get_center(x, y, w, h):
    return int(x + (w / 2)), int(y + (h / 2))

def prep_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.equalizeHist(gray)

def detect_face(frame):
    clean = prep_face(frame)
    small = resize(clean, DETECT_SCALE)
    faces = face_classifier.detectMultiScale(small)
    if len(faces) > 0:
        x, y, w, h = [int(i / DETECT_SCALE) for i in faces[0]]
        center = get_center(x, y, w, h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), BLUE, 2)
        cv2.drawMarker(frame, center, BLUE)
        return center
