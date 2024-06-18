import os
import random

def generate_pantun():
    print("\nGenerate Pantun")
    line1 = random.choice(["Duduk termenung di tepi pantai", "Menikmati kopi di pagi hari"])
    line2 = random.choice(["Sambil menikmati hembusan angin", "Burung berkicau sangat merdu"])
    line3 = random.choice(["Hati ini terasa damai", "Menghangatkan hati yang sepi"])
    line4 = random.choice(["Mengenang masa lalu yang indah", "Menanti masa depan yang cerah"])

    pantun = f"{line1}\n{line2}\n{line3}\n{line4}"
    print("\nGenerated Pantun:")
    print(pantun)

    save_result(pantun, "pantun")

def save_result(result, category):
    if not os.path.exists('output'):
        os.makedirs('output')
    with open(f"output/{category}.txt", "w", encoding="utf-8") as f:
        f.write(result)
    print(f"Result saved in output/{category}.txt")
