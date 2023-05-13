# Vytvořte program, který si nechá na vstupu zadat několik čísel a
# zadávání se ukončí klávesou Enter, což znamená, že vstup
# bude prázdný řetězec. Z těchto čísel se následně vypočítá medián.
# Pro každé zadané číslo program vypíše jeho odchylku od tohoto
# mediánu.

# Create a program that takes several numbers as input and
# typing is terminated with the Enter key, which means that the input
# will be an empty string. The median is then calculated from these numbers.
# For each entered number, the program will print its deviation from this
# the median.

seznam_cisel = []
cislo = 0
print("Zadávej čísla a nakonec zadej pouze ENTER pro ukončení zadávání")
while cislo != "":
    cislo = input("Zadej číslo: ")
    # if cislo.isdigit():
    print(cislo)
    if cislo != "":
        seznam_cisel.append(int(cislo))
    print(seznam_cisel)
seznam_cisel_2 = seznam_cisel.copy()
seznam_cisel_2.sort()
# print(seznam_cisel_2)
median = len(seznam_cisel)//2
# print(median)
# print(seznam_cisel_2[median])
for i in seznam_cisel:
    print(f"{i} se od mediánu odlišuje o {i-seznam_cisel_2[median]}")
# print(seznam_cisel_2)
# print(f"Median: {seznam_cisel_2[median]}")
# print(seznam_cisel)