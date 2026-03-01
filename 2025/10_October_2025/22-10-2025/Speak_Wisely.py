"""Speak Wisely, You Must

Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:

    - Words are separated by a single space.
    - Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".
    - Move all words before and including that word to the end of the sentence and:
        - Preserve the order of the words when you move them.
        - Make them all lowercase.
        - And add a comma and space before them.
    - Capitalize the first letter of the new first word of the sentence.
    - All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
    - Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.

For example, given "You must speak wisely." return "Speak wisely, you must."
"""


def wise_speak(sentence: str) -> str:
    all_key_verbs: list = ["have", "must", "are", "will", "can"]

    all_words: list = sentence[:-1].split(" ")
    words_dict: dict = {i: word for i, word in enumerate(all_words)}
    # print(words_dict)

    the_verbs_present: dict = {
        i: verb for i, verb in words_dict.items() if verb in all_key_verbs
    }
    the_verb_idx: int = next(iter(the_verbs_present))
    the_verb: str = words_dict[the_verb_idx]
    print(the_verb, the_verb_idx)

    sentence_punctuation: str = sentence[-1]
    # print(sentence_punctuation)

    wise_sentence: str = " ".join(
        word for idx, word in enumerate(all_words) if idx > the_verb_idx
    )

    wise_sentence += (
        ", "
        + " ".join(word for idx, word in enumerate(all_words) if idx <= the_verb_idx)
        + sentence_punctuation
    )

    wise_sentence = wise_sentence.capitalize()

    return wise_sentence
