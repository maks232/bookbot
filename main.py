import sys
from stats import get_num_words, get_character_count, get_character_list, sort_character_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_report(filepath):
    contents = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(contents)} total words")
    print("--------- Character Count -------")
    character_list = get_character_list(get_character_count(contents))
    character_list = sort_character_list(character_list)
    for c in character_list:
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    get_report(sys.argv[1])

if __name__ == "__main__":
    main()
