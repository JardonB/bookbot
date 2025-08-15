def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = number_of_words(book_text)
    print(f"{num_words} words found in the document")

def get_book_text(file_path):     #as described; gets the text of the book from input filepath
    with open(file_path) as f:    #takes input file_path and opens it as f
        file_contents = f.read()  #reads contents of f to file_contents
    return file_contents

def number_of_words(input_text):   #determines the number of words in input_text string
    return len(input_text.split()) #split input_text and return the length

main()