from synthesizer import generate_speech
from utility import play_audio
from .config import OUTPUT_AUDIO_PATH

if __name__ == "__main__":
    sample_text = "Artificial Intelligence is transforming the world. From voice assistants to medical diagnoses, AI is improving efficiency and accuracy. The future holds even more exciting possibilities, making our lives smarter and more connected than ever."
    
    generate_speech(sample_text, OUTPUT_AUDIO_PATH)
    print(f"Generated audio saved at: {OUTPUT_AUDIO_PATH}")
    # Play the generated audio
    play_audio(OUTPUT_AUDIO_PATH)