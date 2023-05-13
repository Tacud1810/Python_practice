# Vytvořte program, který si nechá na vstupu zadat 2 intervaly (vždy dolní
# a horní mez jako celé číslo). Následně vypíše všechny dvojice čísel
# (z prvního a druhého intervalu), jejichž součet leží alespoň v jednom z
# intervalů.

# Create a program that accepts 2 intervals (always lower
# and the upper limit as an integer). It then lists all pairs of numbers
# (from the first and second intervals), the sum of which lies in at least one of
# intervals.

leva_mez_1 = int(input("Zadej levou mez 1. intervalu:  "))
prava_mez_1 = int(input("Zadej pravou mez 1. intervalu:  "))
leva_mez_2 = int(input("Zadej levou mez 2. intervalu:  "))
prava_mez_2 = int(input("Zadej pravou mez 2. intervalu:  "))
print("Dvojice čísel, jejichž součet leží alespoň v jednom z intervalů:")
interval_1 = [leva_mez_1, prava_mez_1]
interval_2 = [leva_mez_2, prava_mez_2]
maxi = 0
if max(interval_1)> max(interval_2):
    maxi = max(interval_1)
else:
    maxi = max(interval_2)


for i in range(leva_mez_1,prava_mez_1):
    for j in range(leva_mez_2,prava_mez_2):
        if i+j <= maxi:
            print(f"[{i};{j}]")


# for i in