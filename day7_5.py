

# STEP 1: Import the necessary modules.
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.components import processors
from mediapipe.tasks.python import vision
from fastapi import FastAPI,File, UploadFile
import numpy as np
import cv2
# STEP 2: Create an ImageClassifier object.
base_options = python.BaseOptions(model_asset_path='model\\efficientnet_lite2.tflite')
options = vision.ImageClassifierOptions(
    base_options=base_options, max_results=4)
classifier = vision.ImageClassifier.create_from_options(options)

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    content = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)


    # STEP 4: Classify the input image.
    classification_result = classifier.classify(image)


    # STEP 5: Process the classification result. In this case, visualize it.
    top_category = classification_result.classifications[0].categories[0]
    ret = f"{top_category.category_name} ({top_category.score:.2f})"
    return ret

