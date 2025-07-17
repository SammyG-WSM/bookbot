import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path_to_file = sys.argv[1]

# Function to get the text in the document.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

# Import functions from stats.py

from stats import get_word_count

from stats import get_char_count

from stats import sort_char_count

# Main function
def main():
    # Defining variables
    contents = get_book_text(path_to_file)
    count = get_word_count(contents)
    char_count = get_char_count(contents)
    sorted_char_counts = sort_char_count(char_count)
    
    # Printing the main body
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    # Printing the sorted list of characters
    for item in sorted_char_counts:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    
    print("============= END ===============")
            
main()