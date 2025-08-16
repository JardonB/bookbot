def get_book_text(file_path):     #as described; gets the text of the book from input filepath
    with open(file_path) as f:    #takes input file_path and opens it as f
        file_contents = f.read()  #reads contents of f to file_contents
    return file_contents

def number_of_words(input_text):   #determines the number of words in input_text string
    return len(input_text.split()) #split input_text and return the length

def character_count(input_text):    #counts characters in input_text
    characters = {}                 #empty dictionary to store 'char': count
    for char in input_text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters