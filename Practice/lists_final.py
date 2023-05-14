
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
print(average_student_rating(students))
