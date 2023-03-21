def equilateral(sides):
    a, b, c = sides
    if a or b or c != 0:
        if a + b >= c and a + c >= b and b + c >= a:
            if a == b == c:
                return True
    return False


def isosceles(sides):
    a, b, c = sides
    if a or b or c != 0:
        if a + b >= c and a + c >= b and b + c >= a:
            if a == b or a == c or b == c:
                return True
    return False


def scalene(sides):
    a, b, c = sides
    if a or b or c != 0:
        if a + b >= c and a + c >= b and b + c >= a:
            if equilateral(sides) == True or isosceles(sides) == True:
                return False
            return True
    return False


sides = [3, 2, 3]
print(all(sides))
print(set(sides))
