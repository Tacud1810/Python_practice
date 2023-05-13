# Vytvořte program, který si na vstupu vyžádá postupně koeficienty
# a, b, c kvadratické rovnice
# ax2 + bx + c = 0 a vypočítá její reálné kořeny pomocí
# diskriminantu.
#
# Vzoreček pro výpočet diskriminantu je:
#
# d = b2 - 4 * a * c
#
# A vzoreček pro výpočet kořenů je:
#
#
# 	x1 = (-b + odmocnina(d)) / 2a
#
# 	x2 = (-b - odmocnina(d)) / 2a
#
#
# Komplexními kořeny se nezabývejte, při záporném diskriminantu tedy
# program vypíše, že rovnice nemá řešení.

print("Program for counting quadratic equation.")
print("From of the equation: ax^2 + bx + c = 0 ")

a = float(input("Value a: "))
b = float(input("Value b: "))
c = float(input("Value c: "))
d = (b*b) - (4 * a * c)

if a == 0 or b == 0 or c ==0:
    print("This is not a quadratic equation.")
elif d == 0:
    print("Equation has one root:")
    print(-b / (2*a))
elif d < 0:
    print("Equation has no result in the field of real numbers.")
elif d > 0:
    print("Equation has two roots:")
    print(round((-b + (d**1/2))/2*a))
    print(round((-b - (d**1/2))/2*a))