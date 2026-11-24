
import ollama
import time

# Enter the exact names of your models
MODELS = [
    "llama3.2:1b",
    "lfm3-omni"
]

client = ollama.Client(
    host="http://localhost:11434",
    trust_env=False
)

tasks = [
    {
        "name": "Logical Reasoning",
        "prompt": """
        Petr is taller than Pavel.
        Pavel is taller than Karel.
        Who is the shortest person and why?
        """
    },
    {
        "name": "Mathematics",
        "prompt": """
        A mother buys 3 T-shirts for 250 CZK each
        and 2 pairs of trousers for 450 CZK each.
        The shop gives her a 15% discount on the entire purchase.
        How much does she pay?
        Show your calculation.
        """
    },
    {
        "name": "Programming",
        "prompt": """
        Write a Python function that checks whether
        a given number is a prime number.
        Include three examples of how to use the function.
        """
    },
    {
        "name": "Reading Comprehension",
        "prompt": """
        Jana went to a shop to buy apples.
        She had 100 CZK.
        She bought apples for 35 CZK and bread rolls for 20 CZK.
        On her way home, she found 50 CZK.
        How much money did she have left after shopping?
        """
    },
    {
        "name": "Creativity",
        "prompt": """
        Write a short story about a robot
        that visits a school for the first time.
        The story must contain no more than 100 words.
        """
    }
]

for model in MODELS:

    print("\n" + "=" * 60)
    print("TESTING MODEL:", model)
    print("=" * 60)

    for task in tasks:

        print("\nTASK:", task["name"])

        start_time = time.time()

        try:
            response = client.chat(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": task["prompt"]
                    }
                ]
            )

            end_time = time.time()

            answer = response["message"]["content"]

            print("\nANSWER:")
            print(answer)

            print(
                "\nResponse time:",
                round(end_time - start_time, 2),
                "seconds"
            )

        except Exception as error:
            print("ERROR:", error)

        print("\n" + "-" * 60)

print("\nCOMPARISON COMPLETED!")
