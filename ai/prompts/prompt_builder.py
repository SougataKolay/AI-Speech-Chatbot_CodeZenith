def build_prompt(user_input: str) -> list:
    with open("ai/prompts/behavior_prompt.txt") as f1, open("ai/prompts/formatting_prompt.txt") as f2:
        system_prompt = f"{f1.read().strip()}\n\n{f2.read().strip()}"

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
