"""
Pangram

Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.

    Ignore non-alphabetical characters in the word or sentence.
    Ignore letter casing in the word or sentence.

"""


def is_pangram(sentence, letters) -> bool:
    # make lower case
    sentence: str = sentence.lower()

    # remove non-alphabets (numbers, spaces)
    sentence_alphabets: str = "".join([c for c in sentence if c.isalpha()])

    set_sentence_unique_alphabets: set[str] = set(sentence_alphabets)

    set_given_letters: set[str] = set(letters)

    # find symmetric difference to see if there are extra letters
    difference_letters: set[str] = set_sentence_unique_alphabets ^ set_given_letters

    return not difference_letters


if __name__ == "__main__":
    print(is_pangram("hello", "helo"))
