from Complementary_DNA import complementary_dna


def test_complementary_dna() -> None:
    complementary_dna("ACGT") == "TGCA"
    complementary_dna("ATGCGTACGTTAGC") == "TACGCATGCAATCG"
    complementary_dna("GGCTTACGATCGAAG") == "CCGAATGCTAGCTTC"
    complementary_dna("GATCTAGCTAGGCTAGCTAG") == "CTAGATCGATCCGATCGATC"
