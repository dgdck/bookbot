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

def sort_on(items):
    return items["num"]

def list_dict(my_dict):
    list_of_dicts = [ ]

    for k, v in my_dict.items():
        list_of_dicts.append( { "char": k, "num": v} )
    
    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts


def sorted_list(list):
    for item in list:
        char = item['char']
        num = item['num']
        if char.isalpha():
            print( f'{char}: {num}' )
###### WORK IN PROGRESS ###########
