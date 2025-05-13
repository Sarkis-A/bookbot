import sys
from stats import *

# Gets the contents of a file
def get_book_text(file_path):
    with open(file_path) as book:
        book_contents = book.read()
        return book_contents

# Defines the main function
def main():
    # Get system arguments
    args = sys.argv

    # Check if passed 2 arguments
    # Exits with code 1 if 2 arguments were not passed
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = args[1]
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    sorted_char_list = sort_dict(get_num_char(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_char_list:
        print(f"{i["char"]}: {i["count"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()