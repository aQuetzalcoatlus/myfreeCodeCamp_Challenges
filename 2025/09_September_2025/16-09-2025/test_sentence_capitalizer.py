from Sentence_Capitalizer import capitalize


def test_capitalize() -> None:
    capitalize("this is a simple sentence.") == "This is a simple sentence."
    capitalize("hello world. how are you?") == "Hello world. How are you?"
    capitalize(
        "i did today's coding challenge... it was fun!!"
    ) == "I did today's coding challenge... It was fun!!"
    capitalize(
        "crazy!!!strange???unconventional...sentences."
    ) == "Crazy!!!Strange???Unconventional...Sentences."
    capitalize(
        "there's a space before this period . why is there a space before that period ?"
    ) == "There's a space before this period . Why is there a space before that period ?"
