import cv2

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

    # Apply boundary box obfuscation with modified appearance
    for (x, y, w, h) in faces:
        # Draw a thicker white rectangle around the face region
        cv2.rectangle(image, (x-10, y-10), (x+w+10, y+h+10), (255, 255, 255), 2)  # White rectangle with thickness 2
        # Draw a thinner black rectangle inside the white one
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 0), 1)  # Black rectangle with thickness 1

    # Save the modified image
    cv2.imwrite(output_path, image)

# Usage
disrupt_face_recognition(r'C:\A\TS1.jpg', r'C:\A\TS_obfuscated_faces.jpg')

