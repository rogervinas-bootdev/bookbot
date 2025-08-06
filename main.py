import sys
from stats import get_char_counts, get_num_words

def main(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    print("----------- Word Count ----------")
    num_words = get_num_words(filepath)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = list(get_char_counts(filepath).items())
    char_counts.sort(key=lambda x: x[1], reverse=True)
    for char, count in char_counts:
        print(f"{char}: {count}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        main(filepath)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    