# 1. Create a list of all wagons
# Implement a function get_list_of_wagons() that accepts an arbitrary number of wagon IDs. Each ID will be
# a positive integer. The function should then return the given IDs as a single list.

def get_list_of_wagons(*args):
    return list(args)


# print(get_list_of_wagons(1, 7, 12, 3, 14, 8, 5))

# 2. Fix the list of wagons
# Implement a function fix_list_of_wagons() that takes two lists containing wagon IDs. It should reposition
# the first two items of the first list to the end, and insert the values from the second list behind
# (on the right hand side of) the locomotive ID (1). The function should then return a list with the modifications.

def fix_list_of_wagons(first_list, second_list):
    a, b, c, *last = first_list
    return [c, *second_list, *last, a, b]


# print(fix_list_of_wagons([3, 14, 1, 25, 7, 19, 10], [8, 6, 4, 5, 9, 21, 2, 13]))

# 3. Add missing stops
# Implement a function add_missing_stops() that accepts a routing dict followed by a variable number
# of keyword arguments. These arguments could be in the form of a dict holding one or more stops, or any number
# of stop_number=city keyword pairs. Your function should then return the routing dict updated with an additional
# key that holds a list of all the added stops in order.

def add_missing_stops(route, **kwargs):
    route["stops"] = []
    for key, value in kwargs.items():
        route["stops"].append(value)
    return route



# print(add_missing_stops({"from": "New York", "to": "Miami"},
#                       stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
#                       stop_4="Jacksonville", stop_5="Orlando"))

# 4. Extend routing information
# Implement a function called extend_route_information() that accepts two dicts. The first dict contains
# the origin and destination cities the train route runs between.
# The second dict contains other routing details such as train speed, length, or temperature. The function
# should return a consolidated dict with all routing information.

def extend_route_information(route_information, extended_information):
    return {**route_information, **extended_information}


print(extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"}))


# 5. Fix the wagon depot
# Implement a function called fix_wagon_depot() that accepts a list of three items. Each list item is a sublist
# (or "row") that contains three tuples. Each tuple is a (<wagon ID>, <wagon color>) pair.
# Your function should return a list with the three "row" lists reordered to have the wagons swapped into
# their correct positions.

def fix_wagon_depot(values):
    # print(values)
    a, b, c = zip(*values)
    return [[*a], [*b], [*c]]

# print(fix_wagon_depot([
#                     [(2, "red"), (4, "red"), (8, "red")],
#                     [(5, "blue"), (9, "blue"), (13,"blue")],
#                     [(3, "orange"), (7, "orange"), (11, "orange")],
#                     ]))
