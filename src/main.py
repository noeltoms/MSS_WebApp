from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uuid

from .separator import run_separation

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"
STATIC_DIR = BASE_DIR / "static"

UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

app = FastAPI()

STEMS = ["vocals.wav", "drums.wav", "bass.wav", "other.wav"]


@app.post("/separate")
async def separate(file: UploadFile):
    job_id = str(uuid.uuid4())
    original_ext = Path(file.filename).suffix  # e.g. ".mp3"
    input_path = UPLOAD_DIR / f"{job_id}{original_ext}"

    with open(input_path, "wb") as f:
        f.write(await file.read())

    run_separation(str(input_path), str(OUTPUT_DIR))

    return {
        "job_id": job_id,
        "input_name": input_path.stem,
        "stems": STEMS,
    }


@app.get("/download/{input_name}/{stem}")
def download(input_name: str, stem: str):
    path = OUTPUT_DIR / "htdemucs" / input_name / stem
    return FileResponse(path, filename=stem)


# Serve index.html at "/" — mounted LAST so it doesn't shadow the routes above
app.mount("/", StaticFiles(directory=str(STATIC_DIR), html=True), name="static")