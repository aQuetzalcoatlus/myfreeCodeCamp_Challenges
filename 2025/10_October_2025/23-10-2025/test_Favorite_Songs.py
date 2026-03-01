from Favorite_Songs import favorite_songs


def test_favorite_songs() -> None:
    assert favorite_songs(
        [
            {"title": "Sync or Swim", "plays": 3},
            {"title": "Byte Me", "plays": 1},
            {"title": "Earbud Blues", "plays": 2},
        ]
    ) == ["Sync or Swim", "Earbud Blues"]
    assert favorite_songs(
        [
            {"title": "Skip Track", "plays": 98},
            {"title": "99 Downloads", "plays": 99},
            {"title": "Clickwheel Love", "plays": 100},
        ]
    ) == ["Clickwheel Love", "99 Downloads"]
    assert favorite_songs(
        [
            {"title": "Song A", "plays": 42},
            {"title": "Song B", "plays": 99},
            {"title": "Song C", "plays": 75},
        ]
    ) == ["Song B", "Song C"]
