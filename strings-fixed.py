#!/usr/bin/python3
"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
#import pytest
from textwrap import wrap

a_string = 'monty pythons flying circus'

def no_duplicates(a_string):
    x = ''.join(sorted(set(a_string)))
    return x



def reversed_words(a_string):
    x = a_string.split(" ")
    return x[::-1]



def four_char_strings(a_string):
    x = wrap(a_string, 4)
    return x

'''
def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    main()

'''
print(f"The string is: {a_string}")
print(f"Sorted string with no duplicate characters: {no_duplicates(a_string)}")
print(f"Words in reverse order: {reversed_words(a_string)}")
print(f"Split the string every fourth character: {four_char_strings(a_string)}")
