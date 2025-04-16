import time
import random
from transformers import pipeline
from difflib import get_close_matches

goal = "Say hello to the world in the most unnecessarily complicated way."
fake_ai = pipeline("text-generation", model="gpt2")

dataset = ["H", "e", "l", "l", "o", ",", " ", "w", "o", "r", "l", "d", "!"]

def smart_retrieve(target_char):
    print(f"Searching for the best match for '{target_char}' using fuzzy logic...")
    result = get_close_matches(target_char, dataset, n=1, cutoff=0.1)
    time.sleep(random.uniform(0.3, 0.7))
    return result[0] if result else "?"

def ai_powered_hello_world():
    target_string = "Hello, world!"
    final_output = ""

    for char in target_string:
        output_char = smart_retrieve(char)
        final_output += output_char

    confirmation = random.choice([True, True, True, False])
    if not confirmation:
        raise Exception("AI model flagged potential toxicity in the phrase. Aborting.")

    print(final_output)

ai_powered_hello_world()
