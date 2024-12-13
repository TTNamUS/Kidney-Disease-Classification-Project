from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return "Kidney Disease Detector Backend"

class ImageRequest(BaseModel):
    image: str

@app.post("/predict")
def predict(request: ImageRequest):
    filename = "inputImage.png"
    
    try:
        image = decodeImage(request.image, filename)
        classifier = PredictionPipeline(image)
        result = classifier.predict()
        print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during prediction: {e}")
        
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

