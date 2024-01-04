import cv2
import numpy as np
import time
def facial_recognition(frame):
    # Dictionary mapping reference images to their names
    reference_images = {
        'jonathan.png': 'Jonathan',
        'test.jpg': 'Test'
    }

    # Load the pre-trained Haar cascade classifier for face detection
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Perform facial recognition on the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return False, None

    for (x, y, w, h) in faces:
        # Crop the detected face from the frame
        detected_face = gray[y:y+h, x:x+w]

        for image_path, image_name in reference_images.items():
            # Load the reference image for comparison
            reference_image = cv2.imread(image_path)

            reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

            # Resize the reference image to match the size of the detected face
            resized_reference_gray = cv2.resize(reference_gray, (w, h))

            # Compare the detected face with the reference image using matchTemplate
            result = cv2.matchTemplate(detected_face, resized_reference_gray, cv2.TM_CCOEFF_NORMED)
            threshold = 0.40  # Adjust this threshold as needed
            loc = np.where(result >= threshold)

            # Check if a match is found based on the threshold
            if np.any(result >= threshold):
                # Match found
                return True, image_name

    # No match found
    return False, None

def main():
    # Open the camera
    cap = cv2.VideoCapture(0)
    duration = 3

    # Capture the start time
    start_time = time.time()

    # Loop to continuously capture frames and perform facial recognition
    while time.time() - start_time < duration:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Perform facial recognition on the captured frame
        success, message = facial_recognition(frame)
        print(message)
        # If a match is found, return immediately
        if success:
            # Release the camera
            cap.release()

            # Return the match found message
            return [(success, message)]

    # Release the camera
    cap.release()

    # No match found after processing all frames
    return [(False, "No match found")]
