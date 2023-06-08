import math


# Create the function round_scores() that takes a list of student_scores. This function should consume the input
# list and return a new list with all the scores converted to ints. The order of the scores in the resulting
# list is not important.

def round_scores(student_scores):
    return [round(x) for x in student_scores]


# student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
#
# print(round_scores(student_scores))

# Create the function count_failed_students() that takes a list of student_scores. This function should
# count up the number of students who don't have passing scores and return that count as an integer. A student
# needs a score greater than 40 to achieve a passing grade on the exam.

def count_failed_students(student_scores):
    # x = []
    # for i in student_scores:
    #     if i > 40:
    #         x.append(i)
    return len([grade for grade in student_scores if grade <= 40])


# print(count_failed_students(student_scores=[40, 40, 35, 70, 30, 41, 90]))

# Create the function above_threshold() taking student_scores (a list of grades), and threshold
# (the "top score" threshold) as parameters. This function should return a list of all scores that are >= to threshold.

def above_threshold(student_scores, threshold):
    return [grade for grade in student_scores if grade >= threshold]


# print(above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75))

# Create the function letter_grades() that takes the "highest" score on the exam as a parameter, and returns
# a list of lower score thresholds for each "American style" grade interval: ["D", "C", "B", "A"].

def letter_grades(highest):
    x = []
    x.append(41)
    i = 41
    while i < (highest):
        i = i + ((highest - 41) / 4)
        if i == highest:
            break
        else:
            x.append(math.ceil(i))
    return x


# print(letter_grades(highest=81))

# Create the function student_ranking() with parameters student_scores and student_names. Match each student name
# on the student_names list with their score from the student_scores list. You can assume each argument list will
# be sorted from highest score(er) to lowest score(er). The function should return a list of strings with
#     the format <rank>. <student name>: <student score>.

def student_ranking(student_scores, student_names):
    new_list = []
    for idx, name in enumerate(student_names):
        new_list.append(f"{idx + 1}. {name}: {student_scores[idx]}")
    return new_list


# student_scores = [100, 99, 90, 84, 66, 53, 47]
# student_names = ['Joci', 'Sara', 'Kora', 'Jan', 'John', 'Bern', 'Fred']
# print(student_ranking(student_scores, student_names))

# Create the function perfect_score() with parameter student_info. student_info is a list of lists containing
# the name and score of each student: [["Charles", 90], ["Tony", 80]]. The function should return
# the first [<name>, <score>] pair of the student who scored 100 on the exam.
#
# If no 100 scores are found in student_info, an empty list [] should be returned.

def perfect_score(student_info):
    for student in student_info:
        if student[1]==100:
            return student
    return []

print(perfect_score(student_info=[['Joci', 100], ['Vlad', 100], ['Raiana', 100], ['Alessandro', 100]]))