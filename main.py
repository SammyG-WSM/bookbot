
# Function to get the text in the document.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# Import functions from stats.py

from stats import get_word_count

from stats import get_char_count

# Main function
def main():
    path_to_file = "books/frankenstein.txt"
    contents = get_book_text(path_to_file)
    count = get_word_count(contents)
    c_count = get_char_count(contents)
    
    print(c_count)
    
main()