import sys
from stats import get_num_words, get_num_chars, list_dict, sorted_list


def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    
    return file_contents


def main():
    if len(sys.argv) == 2:
        my_filepath = sys.argv[1]

        print(f'============ BOOKBOT ============')
        print(f'Analyzing book found at {my_filepath}...')
        print(f'----------- Word Count ----------')
        print(
            get_num_words(
            get_book_text( my_filepath )
            )
        )
        print(f'--------- Character Count -------')
        
        sorted_list(
            list_dict(
            get_num_chars(
                get_book_text( my_filepath )
                )
            )
        )
        print('============= END ===============')

    else:
        print( "Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
