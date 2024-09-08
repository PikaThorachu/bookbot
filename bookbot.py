def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    chars_dict = get_num_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- end report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    from string import ascii_letters
    lower_letters = text.lower()
    alpha_lower = "".join([ch for ch in lower_letters if ch in ascii_letters])
    letter_count_dict = {}
    for ch in alpha_lower:
        if ch not in letter_count_dict:
            letter_count_dict[ch] = 1
        else:
            letter_count_dict[ch] += 1
    return letter_count_dict

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()