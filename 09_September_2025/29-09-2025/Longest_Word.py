"""

Given a sentence, return the longest word in the sentence.

    Ignore periods (.) when determining word length.
    If multiple words are ties for the longest, return the first one that occurs.

"""


def get_longest_word(sentence: str) -> str:
    sentence_without_dot: str = "".join(
        character for character in sentence if character != "."
    )
    words_list: list[str] = sentence_without_dot.split(" ")
    words_dict: dict = {word: len(word) for word in words_list}
    sorted_words_dict: dict = dict(
        sorted(words_dict.items(), key=lambda item: item[1], reverse=True)
    )
    return next(iter(sorted_words_dict))


if __name__ == "__main__":
    print(get_longest_word("Peacemaker is bullshit."))
