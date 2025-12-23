def get_num_words(file_contents):
    total_words = len(file_contents.split())
    return f'Found {total_words} total words'


'''
Add a new function to your stats.py file that takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
Convert any character to lowercase using the .lower() method, we don't want duplicates.
Use a dictionary of String -> Integer. The returned dictionary should look something like this:
'''
def get_num_chars(words):
    words_lowcase = words.lower()
    unique_chars = set(words_lowcase)

    letter_dict = { }
    for char in unique_chars:
        count = words_lowcase.count(char)
        letter_dict.update( { char: count} )

    return letter_dict
