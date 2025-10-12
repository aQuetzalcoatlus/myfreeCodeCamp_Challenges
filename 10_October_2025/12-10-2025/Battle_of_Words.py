"""Battle of Words

Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

    - The given sentences will always contain the same number of words.
    - Words are separated by a single space and will only contain letters.
    - The value of each word is the sum of its letters.
    - Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
    - A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
    - Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
    - A word wins if its value is greater than the opposing word's value.
    - The team with more winning words is the winner.

Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.
"""

import string


def letter_score(letter: str) -> int:
    letter_dict: dict = {char: i + 1 for i, char in enumerate(string.ascii_lowercase)}
    letter_dict |= {char: 2 * (i + 1) for i, char in enumerate(string.ascii_uppercase)}

    return letter_dict[letter]


def value(word: str) -> int:
    value: int = 0
    for letter in word:
        value += letter_score(letter)

    return value


def battle(our_team: str, opponent: str, log_word_wins: bool = True) -> str:
    our_words: list[str] = our_team.split(" ")
    their_words: list[str] = opponent.split(" ")

    if len(our_words) != len(their_words):
        raise ValueError("Teams must give the same number of words.")

    word_ranks: list = [i + 1 for i in range(len(our_words))]
    word_scores: dict = {}

    for word_rank, our_word, their_word in zip(word_ranks, our_words, their_words):
        if value(our_word) > value(their_word):
            word_scores[word_rank] = 1
        elif value(our_word) < value(their_word):
            word_scores[word_rank] = 2
        else:
            word_scores[word_rank] = 0

    our_final_score: int = list(word_scores.values()).count(1)
    their_final_score: int = list(word_scores.values()).count(2)

    if our_final_score > their_final_score:
        return "We win"
    elif our_final_score < their_final_score:
        return "We lose"
    else:
        return "Draw"


if __name__ == "__main__":
    print(battle("hello world", "Hello world"))
