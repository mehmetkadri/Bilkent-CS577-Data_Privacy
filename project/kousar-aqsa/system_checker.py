import cv2
import face_recognition

# Load your reference images and encode the face
reference_image = face_recognition.load_image_file("TS2.jpg")
reference_face_encoding = face_recognition.face_encodings(reference_image)[0]

# Load the modified image
test_image = face_recognition.load_image_file("TS_obfuscated_faces.jpg")
test_face_encoding = face_recognition.face_encodings(test_image)

# Check if there's at least one face encoded in the obscured image
if test_face_encoding:
    test_face_encoding = test_face_encoding[0]
    # Compare the faces
    results = face_recognition.compare_faces([reference_face_encoding], test_face_encoding)
    if results[0]:
        print("The face is still recognized")
    else:
        print("The face is NOT recognized")
else:
    print("No face detected in the obscured image.")

