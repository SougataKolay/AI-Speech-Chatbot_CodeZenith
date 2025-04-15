from .models import load_tts_model
from .config import OUTPUT_AUDIO_PATH, LANGUAGE, DEFAULT_SPEAKER

def generate_speech(text, output_path=OUTPUT_AUDIO_PATH, speaker_idx=DEFAULT_SPEAKER, language_idx=LANGUAGE):
    """
    Convert text to speech using the loaded TTS model.
    
    Parameters:
    - text (str): Text to be converted into speech.
    - output_path (str): Path to save the output audio file.
    - speaker_idx (str, optional): Speaker name if the model supports multi-speaker.
    - language_idx (str, optional): Language code if required by the model.
    """

    # Load the model
    tts = load_tts_model()

    # Prepare parameters
    kwargs = {}

    if speaker_idx and speaker_idx in tts.speakers:
        kwargs["speaker"] = speaker_idx  # Some models use "speaker" instead of "speaker_idx"

    if language_idx and language_idx in tts.languages:
        kwargs["language"] = language_idx  # Some models use "language" instead of "language_idx"

    # Synthesize speech and save it
    tts.tts_to_file(text=text, file_path=output_path, **kwargs)
    print(f"Audio file saved at: {output_path}")