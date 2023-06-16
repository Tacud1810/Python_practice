# 1. Clean up Dish Ingredients
# Implement the clean_ingredients(<dish_name>, <dish_ingredients>) function that takes the name of a dish
# and a list of ingredients. This function should return a tuple with the name of the dish as the first item,
# followed by the de-duped set of ingredients.

def clean_ingredients(dish_name, dish_ingredients) -> tuple:
	return (dish_name, set(dish_ingredients))


# 2. Cocktails and Mocktails
# Implement the check_drinks(<drink_name>, <drink_ingredients>) function that takes the name of a drink and a list
# of ingredients. The function should return the name of the drink followed by "Mocktail" if the drink has
# no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol. For the purposes
# of this exercise, cocktails will only include alcohols from the ALCOHOLS constant in sets_categories_data.py:

ALCOHOLS = {"scotch", "whiskey"}


def check_drinks(drink_name, drink_ingredients) -> str:
	if len(ALCOHOLS.intersection(drink_ingredients)) > 0:
		return f"{drink_name} Cocktail"
	else:
		return f"{drink_name} Mocktail"


# 3. Categorize Dishes
# Implement the categorize_dish(<dish_name>, <dish_ingredients>) function that takes a dish name and a set of
# that dish's' ingredients. The function should return a string with the dish name: <CATEGORY> (which meal
# category the dish belongs to). All dishes will "fit" into one of the categories imported
# from sets_categories_data.py (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

def categorize_dish(dish_name, dish_ingredients) -> str:
	if dish_ingredients.issubset(OMNIVORE):
		return f"{dish_name}: OMNIVORE"
	elif dish_ingredients.issubset(KETO):
		return f"{dish_name}: KETO"
	elif dish_ingredients.issubset(PALEO):
		return f"{dish_name}: PALEO"
	elif dish_ingredients.issubset(VEGETARIAN):
		return f"{dish_name}: VEGETARIAN"
	else:
		return f"{dish_name}: VEGAN"


# 4. Label Allergens and Restricted Foods
# Implement the tag_special_ingredients(<dish>) function that takes a tuple with the dish name in the first
# position, and a list or set of ingredients for that dish in the second position. Return the dish name followed
# by the set of ingredients that require a special note on the dish description. Dish ingredients inside a list may
# or may not have duplicates. For the purposes of this exercise, all allergens or special ingredients that need
# to be labeled are in the SPECIAL_INGREDIENTS constant imported from sets_categories_data.py.

SPECIAL_INGREDIENTS = {'garlic', 'soy sauce'}


def tag_special_ingredients(dish: tuple) -> str:
	return (dish[0], set(dish[1]).intersection(SPECIAL_INGREDIENTS))


# 5. Compile a "Master List" of Ingredients
# Implement the compile_ingredients(<dishes>) function that takes a list of dishes and returns a set of all
# ingredients in all listed dishes. Each individual dish is represented by its set of ingredients.

def compile_ingredients(dishes: list) -> set:
	result = set()
	for v in dishes:
		result = result.union(v)
	return result


# 6. Pull out Appetizers for Passing on Trays
# Implement the separate_appetizers(<dishes>, <appetizers>) function that takes a list of dish names and a list
# of appetizer names. The function should return the list of dish names with appetizer names removed. Either
# the <dishes> or <appetizers> list could contain duplicates and may require de-duping.

def separate_appetizers(dishes: list, appetizers: list) -> list:
	return list(set(dishes).difference(set(appetizers)))


# 7. Find Ingredients Used in Only One Recipe
# Implement the singleton_ingredients(<dishes>, <INTERSECTIONS>) function that takes a list of dishes and
# a <CATEGORY>_INTERSECTIONS constant for the same category. Each dish is represented by a set of its ingredients.
# Each <CATEGORY>_INTERSECTIONS is a set of ingredients that appear in more than one dish in the category. Using
# set operations, your function should return a set of "singleton" ingredients (ingredients appearing in only one
# dish in the category).

dishes = [{'black pepper', 'breadcrumbs', 'celeriac', 'chickpea flour',
           'flour', 'lemon', 'parsley', 'salt', 'soy sauce', 'sunflower oil', 'water'},

          {'black pepper', 'cornstarch', 'garlic', 'ginger', 'lemon juice', 'lemon zest',
           'salt', 'soy sauce', 'sugar', 'tofu', 'vegetable oil', 'vegetable stock', 'water'}
          ]
INTERSECTIONS = [{'black pepper', 'garlic', 'lemon juice', 'mixed herbs', 'nutritional yeast',
                  'olive oil', 'salt', 'silken tofu', 'smoked tofu', 'soy sauce', 'spaghetti', 'turmeric'},

                 {'barley malt', 'bell pepper', 'cashews', 'flour', 'fresh basil', 'garlic', 'garlic powder',
                  'honey', 'mushrooms', 'nutritional yeast', 'olive oil', 'oregano', 'red onion',
                  'red pepper flakes', 'rosemary', 'salt', 'sugar', 'tomatoes', 'water', 'yeast'}
                 ]


def singleton_ingredients(dishes, intersection):
	singletons = (dish - intersection for dish in dishes)
	return set.union(*singletons)


print(singleton_ingredients(dishes, INTERSECTIONS))
# singleton_ingredients(dishes, INTERSECTIONS)
