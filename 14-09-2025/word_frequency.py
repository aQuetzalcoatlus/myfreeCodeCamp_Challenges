"""
Given a paragraph, return an array of the three most frequently occurring words.

    Words in the paragraph will be separated by spaces.
    Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
    Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
    The returned array should have all lowercase words.
    The returned array should be in descending order with the most frequently occurring word first.

"""

def get_words(para: str) -> str:
    """
    Remove punctuation - ".", ",", "!"
    Turn to lower case for better count
    """
    # remove punctuation
    para = para.replace(',', '')
    para = para.replace('.', '')
    para = para.replace('!', '')

    # convert to lower case
    para = para.lower()

    # get all words
    words_list: list = para.split(' ')
    words_list.sort()

    # get unique words
    unique_words: list = list(set(words_list))
    unique_words.sort()

    # count occurences
    word_occurences: dict = {}

    for unique_word in unique_words:
        word_occurences[unique_word] = words_list.count(unique_word)

    sorted_dict_desc = dict(sorted(word_occurences.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict_desc)

    top3_words: list = list (sorted_dict_desc.keys())[:3]

    return top3_words

if __name__=='__main__':
    test_paragraph: str = "I like coding. I like testing. I love debugging!"

    print(get_words(test_paragraph))
