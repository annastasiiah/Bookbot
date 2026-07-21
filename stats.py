def count_words(text):
    lenght = len(text.split())
    return lenght

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(item: tuple[str, int]):
    return item[1]

def chars_dict_to_sorted_list(char_count):
    char_list = []
    for char in char_count:
        char_list.append((char, char_count[char]))
    char_list = sorted(char_list, reverse=True, key=sort_on)
    return char_list