"""Tell a Whole Story in 32 Characters — entry for make.fun.

Writes one Wi-Fi network name to /output/entry.txt.
"""
import os

# The joke: a Wi-Fi name that puns on 'it burns when I pee' — a whole story in one name.
TEXT = "It Burns When I WiFi"

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
