import os
import random

def generate_puisi():
    print("\nGenerate Puisi")
    title = random.choice(["The Beauty of Nature", "Love in Silence"])
    verse1 = random.choice(["In the quiet of the night", "Under the moonlit sky"])
    verse2 = random.choice(["Whispers of the wind", "Echoes of the past"])
    verse3 = random.choice(["Touch the soul deeply", "Heal the broken heart"])
    verse4 = random.choice(["Bringing peace and serenity", "Giving hope and new start"])

    puisi = f"{title}\n\n{verse1}\n{verse2}\n{verse3}\n{verse4}"
    print("\nGenerated Puisi:")
    print(puisi)

    save_result(puisi, "puisi")

def save_result(result, category):
    if not os.path.exists('output'):
        os.makedirs('output')
    with open(f"output/{category}.txt", "w", encoding="utf-8") as f:
        f.write(result)
    print(f"Result saved in output/{category}.txt")
