import sys
from stats import count_words, count_characters, chars_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(filepath, num_words, sorted_list):
    print(f"--- Begin report of {filepath} ---")
    print(f"Found {num_words} total words")
    for char, count in sorted_list:
        if not char.isalpha():
            continue

        print(f"{char}: {count}")
    print("--- End report ---")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]

    book = get_book_text(filepath)
    num_words = count_words(book)
    char_count = count_characters(book)
    sorted_list = chars_dict_to_sorted_list(char_count)
    print_report(filepath, num_words, sorted_list)
    
main()  