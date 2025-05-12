from stats import get_num_words, get_num_char

# Gets the contents of a file
def get_book_text(file_path):
    with open(file_path) as book:
        book_contents = book.read()
        return book_contents

# Defines the main function
def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_num_words(book_text)
    char_count = get_num_char(book_text)
    print(f"{word_count} words found in the document")
    print(char_count)

main()