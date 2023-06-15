#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")

    chars = [".", "?", ":"]
    i = 0

    while i in range(len(text)):
        print("{}".format(text[i]), end="")
        if text[i] in chars:
            print("\n")
            while text[i + 1] == " ":
                i += 1
        i += 1
