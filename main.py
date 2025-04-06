from stats import words_counter, chars_counter, get_chars_list
import sys

def get_book_text(path):
    with open(path) as f:
        content = f.read()
        return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    content = get_book_text(path)
    num_words = words_counter(content)
    chars_dict = chars_counter(content)
    chars_list = get_chars_list(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for el in chars_list:
        char = el["char"]
        count = el["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
    

main()