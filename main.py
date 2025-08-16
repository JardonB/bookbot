from stats import get_book_text
from stats import number_of_words
from stats import character_count

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print(f"{number_of_words(book_text)} words found in the document")
    print(character_count(book_text))

main()