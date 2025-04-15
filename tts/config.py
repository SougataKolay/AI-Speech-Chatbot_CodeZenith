import torch

TTS_MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"

LANGUAGE = "en" #default language

DEFAULT_SPEAKER = "Rosemary Okafor"  # Can Change this to any desired speaker

OUTPUT_AUDIO_PATH = "output_audio.wav" # Default output audio path

# Detect if GPU is available
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"