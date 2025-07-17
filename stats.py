# Function to count the number of words in the document.    
def get_word_count(contents):
    words = contents.split()
    return len(words)

# Function to count the number of characters in the document.
def get_char_count(contents):
    text = contents.lower()
    char_count = {}
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count

# Function to sort the individual characters by frequency.

def sort_on(item):
    return item["num"]

def sort_char_count(char_count):
    char_dict = []
    for character, count in char_count.items():
        char_dict.append({"char": character, "num":count})
    char_dict.sort(reverse=True, key=sort_on)
    return char_dict