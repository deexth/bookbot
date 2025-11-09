from stats import list_dict, total_words, char_count
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents, file_path


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    words, file = get_book_text(file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(total_words(words))
    print("--------- Character Count -------")

    list_chars = list_dict(char_count(words))

    for chars in list_chars:
        if chars["char"].isalpha():
            print(f"{chars['char']}: {chars['num']}")

    print("============= END ===============")


main()
