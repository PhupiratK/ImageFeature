import cv2
import numpy as np
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import base64
from app.hog import hog1

def read64(uri):
    img_data =uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(img_data),np.uint8)
    img =cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    return img


app =FastAPI()

@app.get("/")
def root():
    return {"message": "This is my api"}
@app.get("/api/gethog")
async def read_str(request: Request):
    item = await request.json()
    item_str = item['img']
   
    img =read64(item_str)
    hog =hog1(img)
    return {"HOG Descriptor": hog.tolist()}