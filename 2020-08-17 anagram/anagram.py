from collections import Counter
from string import punctuation
from unicodedata import normalize


def clean_unicode_char(c):
    return normalize("NFD", c)[0]


def is_anagram(s1, s2):
    s1_clean = map(clean_unicode_char, s1.lower())
    s2_clean = map(clean_unicode_char, s2.lower())

    s1_letters = filter(str.isalpha, s1_clean)
    s2_letters = filter(str.isalpha, s2_clean)

    s1_count = Counter(s1_letters)
    s2_count = Counter(s2_letters)

    return s1_count == s2_count