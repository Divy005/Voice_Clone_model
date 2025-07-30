import uvicorn
import shutil
from pathlib import Path
import torch

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from TTS.api import TTS

# --- 1. FastAPI App Setup with CORS ---
app = FastAPI()

# Add CORS middleware to allow browser requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. Model Loading (Using YourTTS) ---
# Automatically detect and set the device for model loading
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

print("Loading YourTTS model...")
try:
    # Load the YourTTS model
    tts = TTS("tts_models/multilingual/multi-dataset/your_tts", gpu=(device=="cuda"))
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"An error occurred while loading the model: {e}")
    tts = None

# --- 3. API Endpoints ---
# Create a directory for temporary audio file storage
output_dir = Path("api_outputs")
output_dir.mkdir(exist_ok=True)

@app.get("/")
async def root():
    """Root endpoint to check if the API is running."""
    return {"message": "Voice Cloning API with YourTTS is running."}


@app.post("/synthesize/")
async def synthesize_voice(
    text: str = Form(...),
    voice_sample: UploadFile = File(...)
):
    """Clones a voice from an audio sample and synthesizes the given text."""
    if tts is None:
        return JSONResponse(status_code=500, content={"error": "Model is not loaded."})

    speaker_wav_path = output_dir / voice_sample.filename
    output_wav_path = output_dir / "output.wav"

    # Save the uploaded voice sample file
    with open(speaker_wav_path, "wb") as f:
        shutil.copyfileobj(voice_sample.file, f)

    print(f"Synthesizing text: '{text}'")
    try:
        # Use the YourTTS model to perform the synthesis
        tts.tts_to_file(
            text=text,
            file_path=str(output_wav_path),
            speaker_wav=str(speaker_wav_path),
            language="en"
        )
        print("✅ Synthesis complete!")
        # Return the generated audio file as a response
        return FileResponse(path=str(output_wav_path), media_type="audio/wav", filename="cloned_voice.wav")
    except Exception as e:
        # Handle any errors during the synthesis process
        return JSONResponse(status_code=500, content={"error": f"An internal error occurred: {e}"})

# Note: The uvicorn server is started by the Dockerfile's CMD instruction, not here.
