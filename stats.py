# Counts the words in the book
def get_num_words(file_contents):
    words = file_contents.split()  # Split contents into a list
    word_count = len(words)        # Gets the length of the list
    return word_count

# Counts the character in the book
def get_num_char(file_contents):
    char_dict = {}
    book_text = file_contents.lower()

    # Iterates through each char and adds to dict or increases count
    for char in book_text:
        if char in char_dict:
            current_count = char_dict[char]
            char_dict[char] = current_count + 1
        else:
            char_dict[char] = 1
    
    return char_dict
