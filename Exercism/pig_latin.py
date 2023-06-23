"""
pig latin:
Instructions

Implement a program that translates from English to Pig Latin.

Pig Latin is a made-up children's language that's intended to be confusing. It obeys a few simple rules (below), but
when it's spoken quickly it's really difficult for non-children (and non-native speakers) to understand.

    Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word. Please note that "xr"
    and "yt" at the beginning of a word make vowel sounds (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay").
    Rule 2: If a word begins with a consonant sound, move it to the end of the word and then add an "ay" sound
    to the end of the word. Consonant sounds can be made up of multiple consonants, a.k.a. a consonant cluster
    (e.g. "chair" -> "airchay").
    Rule 3: If a word starts with a consonant sound followed by "qu", move it to the end of the word, and then
    add an "ay" sound to the end of the word (e.g. "square" -> "aresquay").
    Rule 4: If a word contains a "y" after a consonant cluster or as the second letter in a two letter word it
    makes a vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").

"""


VOWELS = {"a", "e", "i", "o", "u"}
VOWELS_Y = {"a", "e", "i", "o", "u", "y"}
SPECIALS = {"xr", "yt"}


def translate(text):
    result = []

    for word in text.split():
        if word[0] in VOWELS or word[0:2] in SPECIALS:
            result.append(word + "ay")
            continue

        for pos in range(1, len(word)):
            if word[pos] in VOWELS_Y:
                pos += 1 if word[pos] == 'u' and word[pos - 1] == "q" else 0
                result.append(word[pos:] + word[:pos] + "ay")
                break

    return " ".join(result)

