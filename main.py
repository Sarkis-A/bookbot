# Gets the contents of a file
def get_book_text(file_path):
    with open(file_path) as book:
        book_contents = book.read()
        return book_contents

# Defines the main function
def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print(book_text)

main()