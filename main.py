from stats import get_num_words, get_num_char, sort_dict

# Gets the contents of a file
def get_book_text(file_path):
    with open(file_path) as book:
        book_contents = book.read()
        return book_contents

# Defines the main function
def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    sorted_char_list = sort_dict(get_num_char(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path[2:]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_char_list:
        print(f"{i["char"]}: {i["count"]}")
    print("============= END ===============")

main()