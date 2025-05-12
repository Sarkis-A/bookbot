# Gets the contents of a file
def get_book_text(file_path):
    with open(file_path) as book:
        book_contents = book.read()
        return book_contents
    
# Splits the text of the file
def content_split(file_contents):
    words = file_contents.split()
    return words

# Defines the main function
def main():
    book_text = get_book_text("./books/frankenstein.txt")
    words_in_book = content_split(book_text)
    word_count = len(words_in_book)
    print(f"{word_count} words found in the document")

main()