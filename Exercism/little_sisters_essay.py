# 1. Capitalize the title of the paper
#
# Any good paper needs a properly formatted title. Implement the function capitalize_title(<title>) which
# takes a title str as a parameter and capitalizes the first letter of each word. This function should return
# a str in title case.

def capitalize(string: str):
    return string.title()


# 2. Check if each sentence ends with a period
#
# You want to make sure that the punctuation in the paper is perfect. Implement the function
# check_sentence_ending() that takes sentence as a parameter. This function should return a bool.

def check_sentence_ending(sentence: str):
    return sentence.endswith(".")


# 3. Clean up spacing
#
# To make the paper look professional, unnecessary spacing needs to be removed. Implement the function
# clean_up_spacing() that takes sentence as a parameter. The function should remove extra whitespace at both
# the beginning and the end of the sentence, returning a new, updated sentence str.

def clean_up_spacing(sentence: str):
    return sentence.strip(' ')

# 4. Replace words with a synonym
#
# To make the paper even better, you can replace some of the adjectives with their synonyms. Write the function
# replace_word_choice() that takes sentence, old_word, and new_word as parameters. This function should replace all
# instances of the old_word with the new_word, and return a new str with the updated sentence.


def replace_word_choice(sentence, what, to):
    return sentence.replace(what, to)


# print(capitalize("ahoj vole"))
print(check_sentence_ending("ahoj vole."))
print(check_sentence_ending("ahoj vole"))
print(' ahoj')
print(clean_up_spacing(" ahoj vole "))
print(replace_word_choice("Ahoj vole", "vole", 'volecku'))
