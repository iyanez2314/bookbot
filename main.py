from sys import argv, exit

from stats import get_char_count, get_num_words, sort_dic_list


def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    print("============ BOOKBOT ===========")
    file_path = argv[1]
    print(f"Analyzing book found at {file_path}...")

    book_text = get_book_text(file_path)
    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)

    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_count = get_char_count(book_text)

    sorted_char_list = sort_dic_list(char_count)

    for char in sorted_char_list:
        print(f"{char['char']}: {char['num']}")

    print("============= END ==============")


main()
