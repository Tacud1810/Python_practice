def eat_ghost(power_pelet_active, touching_ghost):
    return power_pelet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    if power_pellet_active is False and touching_ghost is True:
        return True
    else:
        return False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots == True and lose(power_pellet_active, touching_ghost) == False:
        return True
    else:
        return False
