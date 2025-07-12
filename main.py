from stats import string_count
from stats import letter_count
from stats import sort_character_count
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
filepath = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(filepath)
    word_count = string_count(book_text)
    character_count = letter_count(book_text)
    sorted_chars = sort_character_count(character_count)  # Use character_count instead of char_count_dict

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
    
main()