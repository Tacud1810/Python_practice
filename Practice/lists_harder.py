# 1. Write a function that takes a list of integers as input and returns a new list containing the indices of all
#    the even numbers in the input list.
# 2. Write a program that takes two lists of integers as input and returns a new list containing the elements
#    that are common to both input lists.
# 3. Write a function that takes a list of integers as input and returns the second largest number in the list.
#    If the list contains fewer than two elements, return None.
# 4. Write a program that takes a list of strings as input and returns a new list containing only the strings
#    that are palindromes (i.e., they read the same forwards and backwards).
# 5. Write a function that takes a list of tuples as input, where each tuple contains a name and an age,
#    and returns a new list of names of people who are older than 30.


# ad. 1
def index_of_even(numberlist: list):
    return [idx for idx, i in enumerate(numberlist) if i % 2 == 0]
    # list_of_index = []
    # for idx, i in enumerate(numberlist):
    #     if i % 2 == 0:
    #         list_of_index.append(idx)
    # return list_of_index


# print(index_of_even([4,2,1,4,5,6,7,9,8]))


# ad 2:
def compare_list(first_list: list, second_list: list):
    return [i for i in first_list if i in second_list]


# ad 3
def second_highest_number(number_list: list):
    if len(number_list) <= 2:
        return None
    else:
        number_list.sort()
        return number_list[-2]


# ad 4
def list_of_palindrome(word_list: list):
    return [i for i in word_list if i == i[::-1]]


# ad 5
def sort_by_age(list_of_tuples: list):
    new_list = []
    for i in list_of_tuples:
        if i[1] > 30:
            new_list.append(i[0])
    return new_list
