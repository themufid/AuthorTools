import os
import random

def generate_artikel():
    print("\nGenerate Artikel Blog")
    title = random.choice(["The Benefits of Regular Exercise", "How to Cook Healthy Meals"])
    para1 = random.choice(["Regular exercise is essential for maintaining good health.", 
                           "Cooking healthy meals can be simple and enjoyable."])
    para2 = random.choice(["It helps in improving cardiovascular health, muscle strength, and flexibility.", 
                           "Start with fresh ingredients and balance your meals with proteins, carbs, and fats."])
    para3 = random.choice(["Exercise also boosts mental health by reducing stress and anxiety.", 
                           "Experiment with spices and herbs to add flavor without extra calories."])
    para4 = random.choice(["Incorporate at least 30 minutes of exercise into your daily routine.", 
                           "Plan your meals ahead to ensure you have all the necessary ingredients."])

    artikel = f"{title}\n\n{para1}\n\n{para2}\n\n{para3}\n\n{para4}"
    print("\nGenerated Artikel:")
    print(artikel)

    save_result(artikel, "artikel")

def save_result(result, category):
    if not os.path.exists('output'):
        os.makedirs('output')
    with open(f"output/{category}.txt", "w", encoding="utf-8") as f:
        f.write(result)
    print(f"Result saved in output/{category}.txt")
