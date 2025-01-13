# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 06:34:37 2025

@author: dell
"""
def total_chars(text):
    no_space = 0
    space = text.count(' ')

    for char in text:
        if not char.isspace():
            no_space += 1
            space += 1

    return no_space, space


def total_sentences(text):
    return len(text.split("."))


def display(words,spaces,no_space,sentences):
    print("""
Total Words: {}
Total Characters (With Spaces): {}
Total Characters (Without Spaces): {}
Total Sentences: {}
""".format(words,spaces,no_space,sentences))


def main():
    text = input("Enter text: ")

    if len(text) == 0:
        display(0, 0, 0, 0)
        
    else:
        words = len(text.split())
        spaces, no_space = total_chars(text)
        sentences = total_sentences(text)
        display(words, spaces, no_space, sentences)


if __name__ == "__main__":
    main()