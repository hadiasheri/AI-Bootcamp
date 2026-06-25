import os
import requests

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "openai/gpt-oss-20b:free"


def ask_ai(prompt):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={"model": MODEL, "messages": [{"role": "user", "content": prompt}]},
        timeout=60,
    )

    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]


print("Simple OpenRouter Chatbot")
print("Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ("quit", "exit"):
        break

    try:
        reply = ask_ai(user_input)
        print(f"Bot: {reply}\n")
    except Exception as e:
        print(f"Error: {e}\n")
