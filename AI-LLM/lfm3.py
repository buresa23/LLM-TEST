import ollama

klient = ollama.Client(
    host="http://localhost:11434",
    trust_env=False
)

odpoved = klient.chat(
    model="lfm3-omni",
    messages=[
        {
            "role": "user",
            "content": "Hello, who are you?"
        }
    ]
)

print(odpoved["message"]["content"])