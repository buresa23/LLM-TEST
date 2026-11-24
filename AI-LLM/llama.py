import ollama

klient = ollama.Client(
    host="http://localhost:11434",
    trust_env=False
)

odpoved = klient.chat(
    model="llama3.2:1b",
    messages=[
        {
            "role": "user",
            "content": "Hello, who are you?"
        }
    ]
)

print(odpoved["message"]["content"])