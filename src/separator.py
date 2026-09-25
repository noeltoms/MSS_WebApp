# imports
from demucs.pretrained import get_model
from demucs.apply import apply_model
import torchaudio

model = get_model("htdemucs")  # downloads + caches on first call, loads into memory after
model.eval()

def run_separation_old(input_path: str):
    wav, sr = torchaudio.load(input_path)
    sources = apply_model(model, wav[None])  # runs inference
    return sources  # tensor containing vocals/drums/bass/other


import subprocess


def run_separation(input_path: str, output_dir: str = "outputs") -> None:
    """Runs Demucs on the given file and writes stems into output_dir.

    Demucs will create: <output_dir>/htdemucs/<input_filename_no_ext>/{vocals,drums,bass,other}.wav
    """
    subprocess.run(
        ["demucs", "-o", output_dir, input_path],
        check=True,
    )