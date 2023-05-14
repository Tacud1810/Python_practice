# 1. Write a function that takes a list of numbers as input and returns a new list
#     containing only the even numbers from the input list.
# 2. Write a program that prompts the user to enter a list of words separated by commas and
#     selects from this list the words that start with "a" or "A". Finally, print out these selected words.
# 3. Write a function that takes a list of numbers as input and returns a new list
#     containing only the numbers from the input list that are greater than the average of all
#     the numbers in the list.
# 4. Write a program that takes two different lists of numbers as input and returns a new list
#     containing only the numbers that appear in both input lists.
# 5. Write a function that takes a list of words as input and returns a new list
#     containing the words sorted by length from shortest to longest.


# ad 1.
def even_numbers(input_list):
    result = []
    for number in input_list:
        if number % 2 == 0:
            result.append(number)
    return result


#
#
# # ad 2.
#
list_of_words = input("Give me several words separated by a comma: \n")
words = list_of_words.split(",")

words_start_with_a = []
for i in words:
    if i.strip().startswith("a") or i.strip().startswith("A"):
        words_start_with_a.append(i.strip())
selected_words = [i.strip() for i in words if i.strip()[0] in ["a", "A"]]
print(words_start_with_a)
print(selected_words)


#
#
# # ad 3.
#
def bigger_than_average(list_of_numbers):
    # average = sum(list_of_numbers) / len(list_of_numbers)
    return [
        i for i in list_of_numbers if i > sum(list_of_numbers) / len(list_of_numbers)
    ]
    # for i in list_of_numbers:
    #     if i > average:
    #
    # return average


print(bigger_than_average([10, 2, 5, 8, 6, 4, 156, 23, 236, 99]))


# ad 4.
def compare_list(first_list, second_list):
    return [i for i in first_list if i in second_list]


# ad 5.
def sorted_by_length(wordlist: list):
    return sorted(wordlist, key=len)
