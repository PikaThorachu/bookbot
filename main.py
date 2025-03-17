from stats import get_book_text, get_num_words, get_num_letters, chars_dict_to_sorted_list
import sys

def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    chars_dict = get_num_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("--- end report ---")

main()