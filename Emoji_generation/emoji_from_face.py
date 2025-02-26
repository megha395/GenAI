import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.8)

def detect_facial_expression(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image
    results = face_mesh.process(image_rgb)

    if not results.multi_face_landmarks:
        return "neutral"  # Default if no face detected

    # Extract key points (eyes, eyebrows, mouth)
    face_landmarks = results.multi_face_landmarks[0]

    # Define key landmark indices for facial expressions
    left_eye_top = face_landmarks.landmark[159]  # Upper eyelid
    left_eye_bottom = face_landmarks.landmark[145]  # Lower eyelid
    mouth_top = face_landmarks.landmark[13]
    mouth_bottom = face_landmarks.landmark[14]

    # Calculate distances for eye openness and mouth openness
    eye_openness = abs(left_eye_top.y - left_eye_bottom.y)
    mouth_openness = abs(mouth_top.y - mouth_bottom.y)

    # Classify emotion based on distances
    if mouth_openness > 0.04:
        return "surprise"
    elif eye_openness < 0.02:
        return "angry"
    elif mouth_openness < 0.02:
        return "neutral"
    else:
        return "happy"

emotion_to_emoji = {
    "happy": "😊",
    "neutral": "😐",
    "angry": "😡",
    "surprise": "😮"
}

def get_emoji_from_emotion(emotion):
    return emotion_to_emoji.get(emotion, "😐")  # Default to neutral

