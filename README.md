# Music_Source_Separator_Web_Application
Using trained models to separate music into its stems and available as a web application. 

## Getting Started

### Prerequisites

- Python 3.13
- [Homebrew](https://brew.sh/) (macOS)
- FFmpeg (version 7.x — required by `torchcodec`/`torchaudio` for audio decoding)

Install FFmpeg 7 via Homebrew:
```bash
brew install ffmpeg@7
brew link ffmpeg@7 --force
```

### Setup

1. Clone the repository:
```bash
   git clone https://github.com/noeltoms/MSS_WebApp.git
   cd MSS_WebApp
```

2. Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install --upgrade pip
   pip install -r requirements.txt
```

### Running the app

```bash
uvicorn src.main:app --reload
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

Upload an audio file, wait for processing to complete, and download the separated stems (vocals, drums, bass, other).

### Notes

- The first run will download the Demucs model weights (~300MB+), which are cached locally afterward.
- Uploaded files and separated stems are stored temporarily in `uploads/` and `outputs/` — both are excluded from version control.
