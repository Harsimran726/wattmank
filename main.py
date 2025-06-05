from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import uvicorn
import os
from solarsystem import generate
import base64
from typing import Optional
from fastapi import HTTPException

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...), additional_text: str = None):
    try:
        # Save uploaded file
        file_location = f"temp_{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(await file.read())
        
        # Generate analysis
        result = generate(file_location, additional_text)
        
        # Read the uploaded image and convert to base64
        with open(file_location, "rb") as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
            result["uploaded_image"] = image_base64
        
        # Read the generated image from solarsystem.py if it exists
        if result.get("image_path") and os.path.exists(result["image_path"]):
            with open(result["image_path"], "rb") as generated_image:
                generated_image_base64 = base64.b64encode(generated_image.read()).decode('utf-8')
                result["generated_image"] = generated_image_base64
            # Clean up the generated image file
            os.remove(result["image_path"])
            # Remove the image_path from result as we've converted it to base64
            result.pop("image_path")
        
        # Clean up temporary file
        os.remove(file_location)
        
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
            
        return result
        
    except Exception as e:
        # Clean up any remaining temporary files
        if os.path.exists(file_location):
            os.remove(file_location)
        if result.get("image_path") and os.path.exists(result["image_path"]):
            os.remove(result["image_path"])
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
