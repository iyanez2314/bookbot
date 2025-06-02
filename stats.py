def get_num_words(book_text):
    text = book_text.split()
    length = len(text)
    return length


def get_char_count(book_text):
    char_count = dict()
    for char in book_text:
        char_lowered = char.lower()
        if char_lowered.isalpha():
            char_count[char_lowered] = char_count.get(char_lowered, 0) + 1

    return char_count


def sort_dic_list(dict):
    char_list = [{"char": char, "num": count} for char, count in dict.items()]

    char_list.sort(key=lambda x: x["num"], reverse=True)

    return char_list
