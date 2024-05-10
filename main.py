def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(word_count(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(book):
    return len(book.split())

main()