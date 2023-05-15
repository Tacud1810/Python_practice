# Samozřejmě! Zde je seznam pěti složitějších úkolů, které využívají slovníky v Pythonu:
#
# 1. Úkol: Napište funkci, která vezme jako vstup slovník obsahující jména studentů jako klíče a jejich známky
#    jako hodnoty. Funkce by měla vrátit jména studentů s nejlepším průměrem známek.
#
# 2. Úkol: Napište program, který vezme jako vstup seznam slovníků, přičemž každý slovník obsahuje informace
#    o jednom filmu (název, rok vydání, režisér atd.). Program by měl vrátit seznam filmů, které byly vydány po
#    určitém roce.
#
# 3. Úkol: Napište funkci, která vezme jako vstup slovník obsahující informace o zvířatech (jméno zvířete jako klíč a
#    jeho vlastnosti jako hodnoty). Funkce by měla vrátit seznam zvířat, která mají určité vlastnosti, například zvířata
#    se srstí, zvířata s peřím atd.
#
# 4. Úkol: Napište program, který vezme jako vstup seznam slovníků, přičemž každý slovník obsahuje informace o jednom
#    produktu (název, cena, počet kusů atd.). Program by měl spočítat celkovou hodnotu skladu, tj. součet cen všech
#    produktů na skladě.
#
# 5. Úkol: Napište funkci, která vezme jako vstup slovník obsahující jména studentů jako klíče a jejich předměty
#    a známky jako hodnoty (jiný slovník). Funkce by měla vrátit slovník, ve kterém jsou studenti seřazeni podle
#    průměrného hodnocení předmětů.
#
# Tyto úkoly vám umožní procvičovat práci se slovníky a jejich různými operacemi v Pythonu.

# ad 1:

def best_student(students_dict):
    best_grade_student = {}
    for key, value in students_dict.items():
        best_grade_student.update({key: round(sum(value) / len(value), 2)})
    return sorted(best_grade_student.items(), key=lambda x: x[1])
    # return name for name in best


grades = {
    "John": [85, 92, 78],
    "Emma": [90, 87, 93],
    "Robert": [76, 88, 84],
    "Sophia": [91, 94, 89],
    "Michael": [82, 79, 88]
}


# ad 2:
def films_after_year(list_of_films, year):
    list_of_returned_films = []
    for i in list_of_films:
        if year < i["rok_vydání"]:
            list_of_returned_films.append(i["název"])
    return list_of_returned_films


films = [
    {
        "název": "Pulp Fiction",
        "rok_vydání": 1994,
        "režisér": "Quentin Tarantino"
    },
    {
        "název": "The Shawshank Redemption",
        "rok_vydání": 1994,
        "režisér": "Frank Darabont"
    },
    {
        "název": "Fight Club",
        "rok_vydání": 1999,
        "režisér": "David Fincher"
    },
    {
        "název": "Inception",
        "rok_vydání": 2010,
        "režisér": "Christopher Nolan"
    },
    {
        "název": "The Godfather",
        "rok_vydání": 1972,
        "režisér": "Francis Ford Coppola"
    },
    {
        "název": "Forrest Gump",
        "rok_vydání": 1994,
        "režisér": "Robert Zemeckis"
    },
    {
        "název": "The Dark Knight",
        "rok_vydání": 2008,
        "režisér": "Christopher Nolan"
    },
    {
        "název": "The Matrix",
        "rok_vydání": 1999,
        "režisér": "Lana Wachowski, Lilly Wachowski"
    },
    {
        "název": "Goodfellas",
        "rok_vydání": 1990,
        "režisér": "Martin Scorsese"
    },
    {
        "název": "Schindler's List",
        "rok_vydání": 1993,
        "režisér": "Steven Spielberg"
    }
]

# ad 3:
def animal_trait(animals, animal_trait):
    animal_trait_return = []
    for name, trait in animals.items():
        if animal_trait in trait:
            animal_trait_return.append(name)
    return animal_trait_return

animals = {
    "pes": ["srst", "čtyři nohy", "ostré zuby"],
    "kočka": ["srst", "čtyři nohy", "ostré drápy"],
    "pták": ["peří", "křídla", "zobák"],
    "had": ["šupiny", "beznohý", "jedovatý"],
    "králík": ["srst", "dlouhé uši", "poměrně rychlý"],
    "krokodýl": ["šupiny", "dlouhý ocas", "silné čelisti"]
}

print(animal_trait(animals, "srst"))