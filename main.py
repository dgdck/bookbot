def get_book_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    
    return file_contents


def count_words(file_contents):
    total_words = len(file_contents.split())
    return f'Found {total_words} total words'


def main():
    print(
        count_words(
            get_book_text("books/frankenstein.txt")
        )
    )


main()