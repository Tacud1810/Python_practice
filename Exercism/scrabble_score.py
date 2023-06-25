"""Instructions

Given a word, compute the Scrabble score for that word."""

VALUES_2 = {
    1: "A, E, I, O, U, L, N, R, S, T",
    2: "D, G",
    3: "B, C, M, P ",
    4: "F, H, V, W, Y",
    5: "K",
    8: "J, X",
    10: "Q, Z",
}


def score(word):
    """
    :param word:
    :return: scrabble score
    """
    result = []
    for letter in word.upper():
        result += [key for key, value in VALUES_2.items() if letter in value]
    return sum(result)
