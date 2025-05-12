from stats import get_num_words

# Gets the contents of a file
def get_book_text(file_path):
    with open(file_path) as book:
        book_contents = book.read()
        return book_contents

# Defines the main function
def main():
    book_text = get_book_text("./books/frankenstein.txt")
    words_in_book = get_num_words(book_text)
    print(f"{words_in_book} words found in the document")

main()