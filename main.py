import sys
import os
from modules import pantun, puisi, artikel, copywriting

if sys.stdout.encoding != 'utf-8':
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

def main():
    while True:
        print("\nAuthor Tools")
        print("1. Generate Pantun")
        print("2. Generate Puisi")
        print("3. Generate Artikel Blog")
        print("4. Generate Copywriting Instagram")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            pantun.generate_pantun()
        elif choice == '2':
            puisi.generate_puisi()
        elif choice == '3':
            artikel.generate_artikel()
        elif choice == '4':
            copywriting.generate_copywriting()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
