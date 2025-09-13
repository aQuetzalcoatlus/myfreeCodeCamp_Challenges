def split_words(sentence: str) -> list:
    words_list: list[str] = sentence.split(' ')
    
    words_list_cleaned: list[str] = [word for word in words_list if word]

    return words_list_cleaned

def reverse_words(words_list: list[str]) -> str:
    reversed_list = words_list[::-1]

    reversed_sentence: str = " ".join(word for word in reversed_list)

    return reversed_sentence

def reverse_sentence(given_sentence: str) -> str:
    words_list: list = split_words(given_sentence)
    reversed_sentence: str = reverse_words(words_list)

    return reversed_sentence

print(reverse_sentence('Hello    world!'))