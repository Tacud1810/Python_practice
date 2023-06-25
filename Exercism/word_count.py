"""Instructions

Your task is to count how many times each word occurs in a subtitle of a drama.
The subtitles from these dramas use only ASCII characters.
The characters often speak in casual English, using contractions like they're or it's.
Though these contractions come from two words (e.g. we are), the contraction (we're)
is considered a single word.
Words can be separated by any form of punctuation (e.g. ":", "!", or "?") or whitespace
(e.g. "\t", "\n", or " "). The only punctuation that does not separate words is
the apostrophe in contractions.
Numbers are considered words. If the subtitles say It costs 100 dollars.
then 100 will be its own word.
Words are case insensitive."""

import re

from collections import Counter


def count_words(sentence):
    """counting number of words"""
    return Counter(re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower()))


print(count_words(",\n,one,\n ,two \n 'three'"))
