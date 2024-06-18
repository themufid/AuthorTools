import os
import random

def generate_copywriting():
    print("\nGenerate Copywriting Instagram")
    product = random.choice(["Eco-Friendly Water Bottle", "Wireless Headphones"])
    description = random.choice(["Stay hydrated with our eco-friendly water bottle.", 
                                 "Experience superior sound quality with our wireless headphones."])
    promo = random.choice(["Now available at a special discount!", "Limited time offer, grab yours now!"])
    cta = random.choice(["Order now and enjoy free shipping!", "Buy today and get an exclusive gift!"])
    hashtags = "#EcoFriendly #StayHydrated #SustainableLiving" if "Water Bottle" in product else "#Wireless #Headphones #Music"

    copywriting = (f"🌟 {product} 🌟\n\n{description}\n\n"
                   f"{promo}\n\n{cta}\n\n{hashtags}")
    print("\nGenerated Copywriting:")
    print(copywriting)

    save_result(copywriting, "copywriting")

def save_result(result, category):
    if not os.path.exists('output'):
        os.makedirs('output')
    with open(f"output/{category}.txt", "w", encoding="utf-8") as f:
        f.write(result)
    print(f"Result saved in output/{category}.txt")
