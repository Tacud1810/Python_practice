"""
armstrong number module
"""


def is_armstrong_number(number):
    """

    :param number:
    :return:
    """
    list_number = str(number)
    j = 0
    for i in list_number:
        j += int(i) ** len(list_number)
        # print(i, j)
    # print(j)
    return number == round(j)


print(is_armstrong_number(153))
