"""Dad Joke Showdown entry: write one dad joke to /output/entry.txt."""
import os

JOKE = "Why did the scarecrow win an award? Because he was outstanding in his field."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
