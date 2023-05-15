# 1. Write a function that takes a dictionary where keys are student names and values are lists of their grades,
#    and returns a dictionary where keys are student names and values are their average grades.
# 2. Write a function that takes a list of tuples where each tuple contains a movie title, release year,
#    and IMDb rating, and returns the title of the movie with the highest rating.
# 3. Write a function that takes a dictionary where keys are country names and values are lists of cities in that
#    country, and returns a dictionary where keys are city names and values are the names of the countries they
#    are located in.
# 4. Write a function that takes a dictionary where keys are animal names and values are lists of their
#    food, and returns a list of animals that eat only plant-based food.
# 5. Write a function that takes a list of tuples containing two numerical values, and returns a list of tuples
#    containing the same values, but sorted in ascending order.

# ad 1:
def average_student_rating(students_ratings: dict):
    avg_dict = {}
    for name, grades in students_ratings.items():
        avg = sum(grades) / len(grades)
        avg_dict[name] = avg
    return avg_dict
    # print(i_new)
    # average_rating.update(i_new)
    # return average_rating


students = {
    'Alice': [3, 4, 2, 1],
    'Bob': [2, 5, 4, 3],
    'Charlie': [5, 4, 5, 5],
    'David': [3, 3, 3, 4]
}


# print(average_student_rating(students))
# ad 2:
def highest_rated_movie(movies_list):
    highest_rating = 0
    highest_movie = ""

    for movie in movies_list:
        title, year, rating = movie
        if rating > highest_rating:
            highest_rating = rating
            highest_movie = title

    return highest_movie


# ad 3:
def reverse_dictionary(state_towns):
    town_state = {}
    for key, value in state_towns.items():
        for i in value:
            town_state.update({i: key})
    return town_state


# ad 4:
def plant_food_animal(animalsfood):
    plant_foods = ["carrot", "apple", "lettuce", "peas", "banana", "beetroot", "orange",
                   "parsley", "strawberries", "broccoli", "Grass", "Leaves", "Fruits", "Twigs", "Eucalyptus leaves",
                   "Bamboo", "Hay", "Leafy vegetables"]
    # vege_animals = []
    # for key, value in animalsfood.items():
    #     for i in value:
    #         if i in plant_foods:
    #             if key not in vege_animals:
    #                 vege_animals.append(key)
    # return vege_animals

    vege_animals = []
    for key, value in animalsfood.items():
        if any(food in plant_foods for food in value):
            vege_animals.append(key)
    return vege_animals


animal_food_dict = {
    "Elephant": ["Grass", "Leaves", "Fruits"],
    "Giraffe": ["Leaves", "Twigs", "Fruits"],
    "Koala": ["Eucalyptus leaves"],
    "Panda": ["Bamboo", "Fruits"],
    "Rabbit": ["Grass", "Hay", "Leafy vegetables"],
    "Lion": ["Meat", "Zebra", "Buffalo"],
    "Cheetah": ["Antelope", "Gazelle", "Rabbit"],
    "Wolf": ["Deer", "Elk", "Moose"],
    "Eagle": ["Fish", "Small mammals", "Birds"],
    "Crocodile": ["Fish", "Antelope", "Water birds"],
    "Tiger": ["Meat", "Fish", "Vegetables"],
    "Bear": ["Fish", "Berries", "Honey"],
    "Raccoon": ["Fruits", "Nuts", "Insects"],
    "Fox": ["Small mammals", "Birds", "Grass"],
    "Opossum": ["Fruits", "Insects", "Eggs"]
}


# ad 5:
def sorted_list(list_of_tuples):
    list_of_tuples.sort()
    return list_of_tuples
