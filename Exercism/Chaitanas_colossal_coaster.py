# Define the add_me_to_the_queue() function that takes 4 parameters <express_queue>, <normal_queue>, <ticket_type>,
# <person_name> and returns the appropriate queue updated with the person's name.
#
#     <ticket_type> is an int with 1 == express_queue and 0 == normal_queue.
#     <person_name> is the name (as a str) of the person to be added to the respective queue.


def add_me_to_the_queue(express, normal, ticket_type, person_name):
    if ticket_type == 0:
        normal.append(person_name)
    elif ticket_type == 1:
        express.append(person_name)


# Define the find_my_friend() function that takes 2 parameters queue and friend_name and returns the position
# in the queue of the person's name.
#
#     <queue> is the list of people standing in the queue.
#     <friend_name> is the name of the friend whose index (place in the queue) you need to find.

def find_my_friend(queue, friend_name):
    return queue.index(friend_name)


# Now that their friends have been found (in task #2 above), the late arriver would like to join them at their
# place in the queue. Define the add_me_with_my_friends() function that takes 3 parameters queue, index,
# and person_name.
#
#     <queue> is the list of people standing in the queue.
#     <index> is the position at which the new person should be added.
#     <person_name> is the name of the person to add at the index position.
#
# Return the queue updated with the late arrivals name.


def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index, person_name)
    return queue


# Define the remove_the_mean_person() function that takes 2 parameters queue and person_name.
#
#     <queue> is the list of people standing in the queue.
#     <person_name> is the name of the person that needs to be kicked out.
#
# Return the queue updated without the mean person's name.

def remove_the_mean_person(queue, person_name):
    queue.remove(person_name)
    return queue


# Define the how_many_namefellows() function that takes 2 parameters queue and person_name.
#
#     <queue> is the list of people standing in the queue.
#     <person_name> is the name you think might occur more than once in the queue.
#
# Return the number of occurrences of person_name, as an int.

def how_many_namefellows(queue, person_name):
    return queue.count(person_name)



# Sadly, it's overcrowded at the park today and you need to remove the last person in the normal line
# (you will give them a voucher to come back in the fast-track on another day). You will have to define
# the function remove_the_last_person() that takes 1 parameter queue, which is the list of people standing in
# the queue.
#
# You should update the list and also return the name of the person who was removed, so you can write them a voucher.


def remove_the_last_person(queue):
    return queue.pop()



# Define the sorted_names() function that takes 1 argument, queue,
# (the list of people standing in the queue), and returns a sorted copy of the list.

def sorted_names(queue):
    return sorted(queue)

