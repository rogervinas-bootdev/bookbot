def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(filepath):
    book_text = get_book_text(filepath)
    return len(book_text.split())

def get_char_counts(filepath):
    book_text = get_book_text(filepath)
    char_counts = {}
    for char in book_text:
        char = char.lower()
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts
