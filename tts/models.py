from TTS.api import TTS
from .config import TTS_MODEL_NAME, DEVICE

def load_tts_model():
    """Load the TTS model and return the instance."""
    tts = TTS(model_name=TTS_MODEL_NAME).to(DEVICE)
    return tts

# Example model initialization
if __name__ == "__main__":
    model = load_tts_model()
    print("TTS Model Loaded Successfully!")