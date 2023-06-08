# 1. Extract coordinates
# Implement the get_coordinate() function that takes a (treasure, coordinate) pair from
# Azara's list and returns only the extracted map coordinate.
def get_coordinate(azaras_list):
    return azaras_list[1]


# print(get_coordinate(('Scrimshawed Whale Tooth', '2A')))

# 2. Format coordinates
# Implement the convert_coordinate() function that takes a coordinate in the format "2A"
# and returns a tuple in the format ("2", "A").
def convert_coordinate(coordinates):
    return tuple(coordinates)


# print(convert_coordinate("2A"))

# 3. Match coordinates
# Implement the compare_records() function that takes a (treasure, coordinate) pair and a (location, coordinate,
# quadrant) record and compares coordinates from each. Return True if the coordinates "match", and return
# False if they do not. Re-format coordinates as needed for accurate comparison.
def compare_records(azaras_list, ruis_list):
    return convert_coordinate(get_coordinate(azaras_list)) == ruis_list[1]


# print(compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))
# print(compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple')))

# 4. Combine matched records
# Implement the create_record() function that takes a (treasure, coordinate) pair from Azara's list
# and a (location, coordinate, quadrant) record from Rui's list and returns (treasure, coordinate,
# location, coordinate, quadrant) if the coordinates match. If the coordinates do not match, return
# the string "not a match". Re-format the coordinate as needed for accurate comparison.

def create_record(azaras_list, ruis_list):
    if compare_records(azaras_list, ruis_list):
        return azaras_list + ruis_list
    else:
        return f"not a match"

# print(create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue')))
# print(create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))


# 5. "Clean up" & make a report of all records
# Clean up the combined records from Azara and Rui so that there's only one set of coordinates per record. Make
# a report so they can see one list of everything they need to put on their maps. Implement the clean_up()
# function that takes a tuple of tuples (everything from both lists), looping through the outer tuple, dropping
# the unwanted coordinates from each inner tuple and adding each to a 'report'. Format and return the 'report'
# so that there is one cleaned record on each line.

def clean_up(combined_record_group):
    result = ''
    for record in combined_record_group:
        temp = (record[0], record[2], record[3], record[4])
        result += str(temp) + '\n'
    return result

print(clean_up((
                ('Scrimshawed Whale Tooth', '2A', 'Deserted Docks', ('2', 'A'), 'Blue'),
                ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'),
                ('Robot Parrot', '1C', 'Seaside Cottages', ('1', 'C'), 'Blue'),
                ('Glass Starfish', '6D', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange'),
                ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'),
                ('Pirate Flag', '7F', 'Windswept Hilltop (Island of Mystery)', ('7', 'F'), 'Orange'),
                ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'),
                ('Model Ship in Large Bottle', '8A', 'Harbor Managers Office', ('8', 'A'), 'Purple'),
                ('Angry Monkey Figurine', '5B', 'Stormy Breakwater', ('5', 'B'), 'Purple'),
                ('Carved Wooden Elephant', '8C', 'Foggy Seacave', ('8', 'C'), 'Purple'),
                ('Amethyst  Octopus', '1F', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow'),
                ('Antique Glass Fishnet Float', '3D', 'Spiky Rocks', ('3', 'D'), 'Yellow'),
                ('Silver Seahorse', '4E', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')
        )))