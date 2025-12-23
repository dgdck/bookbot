from stats import get_num_words, get_num_chars


def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    
    return file_contents


def main():
    print(
        get_num_words(
            get_book_text("books/frankenstein.txt")
        )
    )
    print(
        get_num_chars(
            get_book_text("books/frankenstein.txt")
        )
    )


main()