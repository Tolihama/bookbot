def words_counter(string):
    return len(string.split())

def chars_counter(string):
    chars = string.lower()
    chars_dict = {}

    for char in chars:
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1

    return chars_dict

def get_chars_list(chars_dict):
    def sort_on(dict):
        return dict["count"]

    c_list = []
    for key in chars_dict:
        item = {
            "char": key,
            "count": chars_dict[key]
        }
        c_list.append(item)

    c_list.sort(reverse=True, key=sort_on)
    return c_list