#!/usr/bin/python3
def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of
    these characters: ., ? and :

    Args:
        text: text to indent
    Raises:
        TypeError:
            text must be a string
    """

    tmp = '.'

    if type(text) is not str:
        raise TypeError('text must be a string')

    text = text.strip()

    for letter in text:
        if letter == ' ' and tmp in '.:?':
            continue
        print('{}'.format(letter), end='')
        tmp = letter
        if letter in '.:?':
            print('\n')
