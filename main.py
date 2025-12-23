from stats import get_num_words, get_num_chars, list_dict, sorted_list


def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    
    return file_contents


def main():
    print(f'============ BOOKBOT ============')
    print(f'Analyzing book found at books/frankenstein.txt...')
    print(f'----------- Word Count ----------')
    print(
        get_num_words(
        get_book_text("books/frankenstein.txt")
        )
    )
    print(f'--------- Character Count -------')
    
    sorted_list(
        list_dict(
        get_num_chars(
            get_book_text("books/frankenstein.txt")
            )
        )
    )

    print('============= END ===============')

main()