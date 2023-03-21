import string


def is_pangram(sentence):
    alphabet = list(string.ascii_lowercase)
    sentence = sentence.lower()
    for i in alphabet:
        if i not in sentence:
            return False
    return True

print(is_pangram("The quick brown fox jumps over the lazy dog."))
