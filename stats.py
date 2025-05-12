# Counts the words of the file
def get_num_words(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count