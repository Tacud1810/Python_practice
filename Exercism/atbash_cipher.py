"""Instructions

Given a word, compute the Scrabble score for that word."""

PLAIN = "abcdefghijklmnopqrstuvwxyz"
CIPHER = "zyxwvutsrqponmlkjihgfedcba"


def encode(plain_text):
    """encoding"""
    result = ""
    clean_text = "".join(a.lower() for a in plain_text if a.isalnum())
    for letter in clean_text:
        if letter.isnumeric():
            result += letter
        else:
            result += CIPHER[PLAIN.index(letter)]
    return " ".join(result[i : i + 5] for i in range(0, len(result), 5))


def decode(plain_text):
    """decoding"""
    result = ""
    for letter in plain_text.lower():
        if letter == " ":
            continue
        if letter.isnumeric():
            result += letter
        else:
            result += CIPHER[PLAIN.index(letter)]
    return result


# print(decode("gvhgr mt123 gvhgr mt"))
def cleanup(plain_text):
    """cleaning the text"""
    return "".join(a.lower() for a in plain_text if a.isalnum())


def encode_2(plain_text):
    """final version of encoding"""
    result = cleanup(plain_text)
    result = result.translate(plain_text.maketrans(PLAIN, CIPHER))
    return " ".join(result[i : i + 5] for i in range(0, len(result), 5))


print(encode_2("ahoj123,."))
