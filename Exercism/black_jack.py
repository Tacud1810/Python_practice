def value_of_card(card):
    if card == "J" or card == "Q" or card == "K":
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    if int(value_of_card(card_one)) == int(value_of_card(card_two)):
        return card_one, card_two
    elif int(value_of_card(card_one)) > int(value_of_card(card_two)):
        return card_one
    else:
        return card_two


def value_of_ace(card_one, card_two):
    # if card_one == "A" and card_two == "A":
    #     return 1
    # elif card_one == "A":
    #     if int(value_of_card(card_two)) < 10:
    #         return 11
    #     else:
    #         return 1
    # elif card_two == "A":
    #     if int(value_of_card(card_one)) < 10:
    #         return 11
    #     else:
    #         return 1
    # elif int(value_of_card(card_one)) + int(value_of_card(card_two)) <= 10:
    #     return 11
    # else:
    #     return 1
    # print(value_of_card(card_one))
    # print((value_of_card(card_two)))
    if card_one == "A" or card_two == "A":
        return 1
    elif (int(value_of_card(card_one)) + int(value_of_card(card_two))) <= 10:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    if card_one == "A":
        # print()
        # print(int(value_of_ace(card_one, card_two)))
        if int(value_of_card(card_two)) == 10:
            return True
        else:
            return False
    elif card_two == "A":
        if int(value_of_card(card_one)) == 21:
            return True
        else:
            return False
    elif int(value_of_ace(card_one, card_two)) + int(value_of_card(card_two)) < 21:
        return False
    else:
        return True


def can_split_pairs(card_one, card_two):
    if int(value_of_card(card_one)) == int(value_of_card(card_two)):
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    print(f"{int(value_of_card(card_one)) + int(value_of_card(card_two))}")
    if 9 <= int(value_of_card(card_one)) + int(value_of_card(card_two)) <= 11:
        return True
    else:
        return False
