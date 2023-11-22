import os
import re

def replace_please(text):
    while True:
        match = re.search(r"(?<!\w)please(?!\w)", text, flags=re.IGNORECASE)
        if not match:
            break

        start = match.start()
        end = match.end()
        next_word = text[end:].split()[0]

        if start == 0:
            next_word = next_word.capitalize()

        replacement = next_word
        text = text[:start] + replacement + text[end:]

    return text

def scan_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            filepath = os.path.join(folder_path, filename)

            with open(filepath, "r", encoding="utf8") as f:
                text = f.read()

            text = replace_please(text)

            with open(filepath, "w", encoding="utf8") as f:
                f.write(text)

if __name__ == "__main__":
    folder_path = "path/to/folder"
    scan_folder(folder_path)
