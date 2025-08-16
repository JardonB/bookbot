import sys
from stats import get_book_text, number_of_words, character_count, sort_on, dict_to_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)       
    path = sys.argv[1]
    book_text = get_book_text(path)
    chars_count = dict_to_list(character_count(book_text))
    chars_count.sort(reverse=True, key=sort_on)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...")
    print(f"----------- Word Count ----------\nFound {number_of_words(book_text)} total words")
    print("--------- Character Count -------")
    for i in range(0, len(chars_count)):
        if chars_count[i]["char"].isalpha():
            print(f"{chars_count[i]["char"]}: {chars_count[i]["num"]}")
    print("============= END ===============")

main()