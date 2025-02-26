from emoji_from_face import *
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Face to Emoji API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_path = await file.read()
    emotion = detect_facial_expression(image_path)
    emoji = get_emoji_from_emotion(emotion)

    return {"emotion": emotion, "emoji": emoji}
