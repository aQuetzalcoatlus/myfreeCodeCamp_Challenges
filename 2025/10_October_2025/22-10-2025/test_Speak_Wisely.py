from Speak_Wisely import wise_speak


def test_wise_speak() -> None:
    wise_speak("You must speak wisely.") == "Speak wisely, you must."
    wise_speak("You can do it!") == "Do it, you can!"
    wise_speak(
        "Do you think you will complete this?"
    ) == "Complete this, do you think you will?"
    wise_speak("All your base are belong to us.") == "Belong to us, all your base are."
    wise_speak("You have much to learn.") == "Much to learn, you have."
