import cv2
import numpy as np

def disrupt_face_recognition(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found")
        return

    # Convert image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained face detection model from OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Apply aggressive feature obfuscation while maintaining recognizability for humans
    for (x, y, w, h) in faces:
        # Extract the face region
        face_region = image[y:y+h, x:x+w]

        # Darken the eyes
        eye_y_shift = int(h * 0.25)
        eye_h_shift = int(h * 0.2)
        face_region[y + eye_y_shift:y + eye_y_shift + eye_h_shift, x:x + w] = [0, 0, 0]

        
        # Add noise to the nose region
        # nose_y_shift = int(h * 0.45)
        # nose_h_shift = int(h * 0.4)
        # # Ensure noise array has the same shape as the region where it's being added
        # noise = np.random.randint(-20, 20, (nose_h_shift, w, 3), dtype=np.int16)
        # noise = noise[:h - nose_y_shift - nose_h_shift, :w, :]
        # face_region[y + nose_y_shift:y + nose_y_shift + noise.shape[0], x:x + w] += noise.astype(np.uint8)






        # Darken the mouth and chin
        mouth_y_shift = int(h * 0.7)
        mouth_h_shift = int(h * 0.3)
        face_region[y + mouth_y_shift:y + mouth_y_shift + mouth_h_shift, x:x + w] = [0, 0, 0]

        # Replace the face region with the modified one
        image[y:y+h, x:x+w] = face_region

    # Save the modified image
    cv2.imwrite(output_path, image)

# Usage
disrupt_face_recognition("TS1.jpg", "Salient_Feature_TS.jpg")

