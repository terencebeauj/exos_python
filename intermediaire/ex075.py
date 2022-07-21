from logging import debug
import string

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

def word_counter(lorem):
    punctuation = string.punctuation
    for char in punctuation:
        lorem = lorem.replace(char, "")
    array = lorem.lower().split()
    return array.count('elit')


print(word_counter(lorem))