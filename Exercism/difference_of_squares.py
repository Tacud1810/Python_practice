def square_of_sum(number):
    # j = 0
    # for i in range(number+1):
    #     j += i
    #     # print(j)
    # return j**2
    return sum(i for i in range(number +1))**2


def sum_of_squares(number):
    # j = 0
    # for i in range(number+1):
    #     j += i**2
    # return j
    return sum(i**2 for i in range(number +1))


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)


print(square_of_sum(3))
print(sum_of_squares(3))
print(difference_of_squares(3))