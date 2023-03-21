EXPECTED_BAKE_TIME= 40
PREPARATION_TIME = 2


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    return number_of_layers*PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
       Return elapsed cooking time.

       This function takes two numbers representing the number of layers & the time already spent
       baking and calculates the total elapsed minutes spent cooking the lasagna.
       """
    return ((PREPARATION_TIME * number_of_layers) + (EXPECTED_BAKE_TIME-elapsed_bake_time))
