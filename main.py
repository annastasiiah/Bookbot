from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words(book)
    print(f'Found {num_words} total words')

main()  