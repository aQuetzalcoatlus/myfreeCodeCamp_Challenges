"""Complementary DNA

Given a string representing a DNA sequence, return its complementary strand using the following rules:

    - DNA consists of the letters "A", "C", "G", and "T".
    - The letters "A" and "T" complement each other.
    - The letters "C" and "G" complement each other.

For example, given "ACGT", return "TGCA".
"""


def complementary_dna(strand: str) -> str:
    DNA_letters: set[str] = {"A", "C", "G", "T"}
    invalid_chars: int = sum(1 for ch in strand if ch not in DNA_letters)

    if invalid_chars:
        raise ValueError(f"Given strand should only contain characters {DNA_letters}")

    complements_dict: dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complement_strand: str = "".join(complements_dict[char] for char in strand)

    return complement_strand


if __name__ == "__main__":
    print(complementary_dna("ATGCGTACGTTAGC"))
