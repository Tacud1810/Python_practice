def square(number):
    # try:
        # if number == 0:
        #     return 0
    if number == 1:
        return 1
    elif 2 <= number <= 64:
        count = 2
        for i in range(2, number):
            count = count * 2
        return count
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    # try:
        # if number == 0:
        #     return 0
    # if number == 1:
    #     return 1
    # elif 2 <= number <= 64:
        count = 2
        total = 3
        for i in range(2, 64):
            count = count * 2
            total += count
        return total
    # else:
    #     raise ValueError("square must be between 1 and 64")


print(square(64))
print(total())