def main():
    book_file = "books/frankenstein.txt"
    text = get_text(book_file)
    w_count = word_count(text)
    l_count = letter_count(text)
    l_sort = sorted_letters(l_count)
    print(f"~~~ A report of the contents of {book_file} ~~~")
    print()
    print(f"The document contains {w_count} words.")
    print()
    for l in l_sort:
        if l["char"].isalpha():
            print(f"The character '{l['char']}' was found {l['count']} times.")
    print()
    print("~~~ End of Report ~~~")
            
def get_text(path):
    with open(path) as f:
        return f.read()

def word_count(book):
    return len(book.split())

def letter_count(book):
    lowered_book = book.lower()
    char_count = {}
    for char in lowered_book:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_key(k):
    return k["count"]

def sorted_letters(char_dict):
    sorted_ls = []
    for char in char_dict:
        sorted_ls.append({"char": char, "count": char_dict[char]})
    sorted_ls.sort(reverse=True, key=sort_key)
    return sorted_ls

main()