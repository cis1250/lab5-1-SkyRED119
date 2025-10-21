#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence() -> str:
    user_sentence = input("Enter a sentence: ")

    while (is_sentence(user_sentence) == False):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")
    
    return user_sentence


def clean_up_sentence(sentence: str) -> str:
    sentence = sentence.lower()
    clean_sentence = ""

    for r in sentence:
        if r.isalpha() or r.isspace():
            clean_sentence += r

    return clean_sentence


def calculate_frequencies(sentence: str) -> ([], []):
    sentence = clean_up_sentence(sentence)
    sentence = sentence.split()
    words = []
    frequency = []

    for i in sentence:
        if i in words:
            frequency[words.index(i)] += 1
            continue
        words.append(i)
        frequency.append(1)

    return words, frequency


def print_frequencies(words: [], frequencies: []) -> None:
    for j in range(len(words)):
        print(f"{words[j]}: {frequencies[j]}")


def main():
    sentence = get_sentence()
    sentence_information = calculate_frequencies(sentence)
    print_frequencies(sentence_information[0], sentence_information[1])


main()
