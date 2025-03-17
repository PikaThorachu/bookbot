from stats import get_book_text, get_num_words, get_num_letters, chars_dict_to_sorted_list

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    chars_dict = get_num_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("--- end report ---")

main()