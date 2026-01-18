import sys

from stats import count_words

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  with open(sys.argv[1]) as f:
    file_contents = f.read()

    print(f"--- Begin report of {sys.argv[1]} ---")

    num_words = count_words(file_contents)
    print(f"Found {num_words} total words\n")

    num_characters = count_characters(file_contents)
    for item in num_characters:
      print(f"'{item["character"]}: {item["count"]}'")

    print("--- End report ---")


def sort_on(dict):
  return dict["count"]


def count_characters(text):
  text = text.lower()
  char_count = {}

  for char in text:
    if char.isalpha():
      char_count[char] = char_count.get(char, 0) + 1

  # Convert the dictionary to a list of dictionaries
  characters = [{"character": char, "count": count} for char, count in char_count.items()]

  # Sort the list by count in descending order
  characters.sort(reverse=True, key=sort_on)

  return characters


main()