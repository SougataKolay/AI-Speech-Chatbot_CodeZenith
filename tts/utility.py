import sounddevice as sd
import soundfile as sf

def play_audio(file_path):
    """Plays an audio file."""
    audio_data, sample_rate = sf.read(file_path)
    sd.play(audio_data, samplerate=sample_rate)
    sd.wait()