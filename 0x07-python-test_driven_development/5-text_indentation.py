#!/usr/bin/python3
def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = True
    for char in text:
        if char in ".?:":
            print(char, end="")
            print("\n\n", end="")
            new_line = True
        elif char == " " and new_line:
            continue
        else:
            print(char, end="")
            new_line = False
