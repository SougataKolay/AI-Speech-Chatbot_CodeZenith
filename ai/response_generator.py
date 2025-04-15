import ollama
from ai.config import AI_MODEL, TEMPERATURE, TOP_P, MAX_TOKENS
from ai.prompts.prompt_builder import build_prompt

def generate_response(user_input: str) -> str:
    """Generates a cleaned, corrected response using LLaMA."""
    messages = build_prompt(user_input)

    response = ollama.chat(
        model=AI_MODEL,
        messages=messages,
        options={
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
            "num_predict": MAX_TOKENS
        }
    )

    return response["message"]["content"].strip()
