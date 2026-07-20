def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    lenght = len(text.split())
    return lenght

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words(book)
    print(f'Found {num_words} total words')

main()  