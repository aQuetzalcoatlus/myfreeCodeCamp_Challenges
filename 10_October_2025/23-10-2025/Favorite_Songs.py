"""Favorite Songs

Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

    Each object will have a "title" property (string), and a "plays" property (integer).

"""


def favorite_songs(playlist: list[dict[str, int | str]]) -> list[str]:
    proper_playlist_dict: dict = {
        song_dict["title"]: song_dict["plays"] for song_dict in playlist
    }
    sorted_playlist: list = sorted(
        proper_playlist_dict.items(), key=lambda kv: kv[1], reverse=True
    )
    return [title for title, _ in sorted_playlist][:2]


if __name__ == "__main__":
    print(
        favorite_songs(
            [
                {"title": "Sync or Swim", "plays": 3},
                {"title": "Byte Me", "plays": 1},
                {"title": "Earbud Blues", "plays": 2},
            ]
        )
    )
