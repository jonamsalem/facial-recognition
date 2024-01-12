import cv2
import numpy as np
import time
import smtplib
from dotenv import load_dotenv
import os
import tempfile
import imghdr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

load_dotenv()
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')
smtp_username = os.getenv('SMTP_USERNAME')
smtp_password = os.getenv('SMTP_PASSWORD')

def facial_recognition(frame):
    images_directory = 'images/'
    # Dictionary mapping reference images to their names
    image_files = [f for f in os.listdir(images_directory) if os.path.isfile(os.path.join(images_directory, f))]

    # Create the reference_images dictionary dynamically
    reference_images = {}
    for filename in image_files:
        # Add the image file to the dictionary with its name (without extension) as the key
        reference_images[os.path.join(images_directory, filename)] = os.path.splitext(filename)[0]  
        # Load the pre-trained Haar cascade classifier for face detection
        face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Perform facial recognition on the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return False, None, None  # Return False and None for message and matched_face when no faces are found

    for (x, y, w, h) in faces:
        detected_face = gray[y:y+h, x:x+w]

        for image_path, image_name in reference_images.items():
            reference_image = cv2.imread(image_path)
            reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
            resized_reference_gray = cv2.resize(reference_gray, (w, h))

            # Compare the detected face with the reference image using matchTemplate
            result = cv2.matchTemplate(detected_face, resized_reference_gray, cv2.TM_CCOEFF_NORMED)
            threshold = 0.40 
            loc = np.where(result >= threshold)

            # Check if a match is found based on the threshold
            if np.any(result >= threshold):
                return True, image_name, detected_face  # Return True, image_name, and detected_face when a match is found

    return False, None, None  # Return False and None for message and matched_face when no match is found

def send_email_with_attachment(subject, body, attachment_path):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = smtp_username
    msg['Subject'] = subject

    # Attach the image to the email
    with open(attachment_path, 'rb') as img_file:
        img = MIMEImage(img_file.read(), _subtype=imghdr.what(img_file.name))
        img.add_header('Content-Disposition', 'attachment', filename='matched_face.png')
        msg.attach(img)

    # Add the message body
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=smtp_username, password=smtp_password)
        connection.sendmail(smtp_username, smtp_username, msg.as_string())

def main(method):
    if method == 'GET':
        # Open the camera
        cap = cv2.VideoCapture(0)
        duration = 3
        start_time = time.time()

        # Loop to continuously capture frames and perform facial recognition
        while time.time() - start_time < duration:
            # Capture a frame from the camera
            ret, frame = cap.read()

            # Perform facial recognition on the captured frame
            success, message, matched_face = facial_recognition(frame)

            # If a match is found, send an email
            if success:
                # Save the matched face as a temporary image file
                _, temp_image_path = tempfile.mkstemp(suffix='.png')
                cv2.imwrite(temp_image_path, matched_face)

                # Send the email with the matched face as an attachment
                send_email_with_attachment('Facial Recognition App', f'Face recognized: {message}', temp_image_path)
                os.remove(temp_image_path)
                return (success, message)

        return (False, "No match found")
    elif method == 'POST':
        cap = cv2.VideoCapture(0)
        duration = 1.5
        start_time = time.time()

        # Loop to continuously capture frames and perform facial recognition
        while time.time() - start_time < duration:
            ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        cap.release()
        # Check if a face is detected
        if len(faces) > 0:
            x, y, w, h = faces[0]
            cropped_frame = frame[y:y+h, x:x+w]

            # Save the cropped frame as an image under the "images" directory
            image_filename = f"captured_face_{int(time.time())}.png"
            image_path = os.path.join("images", image_filename)
            cv2.imwrite(image_path, cropped_frame)
            return (True, "face detected and saved")
        else: 
            return (False, "no face detected ")
        
if __name__ == "__main__":
    main()
