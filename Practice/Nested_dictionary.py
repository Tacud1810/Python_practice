# 1. Úkol: Napište program, který pracuje se seznamem knih. Každá kniha je reprezentována slovníkem
# s následujícími informacemi: název knihy, autor, rok vydání a hodnocení. Program by měl umožnit
# uživateli vyhledávat knihy podle různých kritérií, jako je autor nebo rok vydání.
#
# 2. Úkol: Vytvořte program pro správu filmů ve filmové kolekci. Každý film je reprezentován slovníkem
# obsahujícím název filmu, režiséra, rok vydání a seznam herců. Program by měl umožnit uživateli přidávat,
# upravovat a vyhledávat filmy v kolekci.
#
# 3. Úkol: Napište program pro evidenci zaměstnanců ve firmě. Každý zaměstnanec je reprezentován slovníkem
# s informacemi jako jméno, příjmení, pozice a plat. Program by měl umožnit uživateli přidávat, upravovat
# a vyhledávat zaměstnance na základě různých kritérií, jako je pozice nebo plat.


books = [
    {
        "název": "Válka světů",
        "autor": "H.G. Wells",
        "rok_vydání": 1898,
        "hodnocení": 4.5,
    },
    {"název": "1984", "autor": "George Orwell", "rok_vydání": 1949, "hodnocení": 4.7},
    {
        "název": "Harry Potter a kámen mudrců",
        "autor": "J.K. Rowling",
        "rok_vydání": 1997,
        "hodnocení": 4.8,
    },
    {
        "název": "Pán prstenů: Společenstvo prstenu",
        "autor": "J.R.R. Tolkien",
        "rok_vydání": 1954,
        "hodnocení": 4.9,
    },
    {
        "název": "Vlkodlak",
        "autor": "Stephen King",
        "rok_vydání": 1985,
        "hodnocení": 4.2,
    },
]

films = [
    {
        "název": "Pulp Fiction",
        "režisér": "Quentin Tarantino",
        "rok_vydání": 1994,
        "herci": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"],
    },
    {
        "název": "Vykoupení z věznice Shawshank",
        "režisér": "Frank Darabont",
        "rok_vydání": 1994,
        "herci": ["Tim Robbins", "Morgan Freeman"],
    },
    {
        "název": "Forrest Gump",
        "režisér": "Robert Zemeckis",
        "rok_vydání": 1994,
        "herci": ["Tom Hanks", "Robin Wright", "Gary Sinise"],
    },
    {
        "název": "Matrix",
        "režisér": "Lana Wachowski",
        "rok_vydání": 1999,
        "herci": ["Keanu Reeves", "Carrie-Anne Moss", "Hugo Weaving"],
    },
    {
        "název": "Pán prstenů: Návrat krále",
        "režisér": "Peter Jackson",
        "rok_vydání": 2003,
        "herci": ["Elijah Wood", "Viggo Mortensen", "Ian McKellen"],
    },
    {
        "název": "Pán prstenů: Společenstvo prstenu",
        "režisér": "Peter Jackson",
        "rok_vydání": 2001,
        "herci": ["Elijah Wood", "Viggo Mortensen", "Ian McKellen"],
    }
]

employees = {
    "John Doe": {"pozice": "Manažer", "plat": 5000},
    "Jane Smith": {"pozice": "Asistentka", "plat": 2500},
    "Michael Johnson": {"pozice": "Programátor", "plat": 4000},
    "Emily Davis": {"pozice": "Grafik", "plat": 3000},
    "David Brown": {"pozice": "Administrativní pracovník", "plat": 2800},
}


# ad 1:
def searching_by_name(list_of_books, value):
    for book in list_of_books:
        for names, key in book.items():
            if value == key:
                return f"Kniha hledána podle: {value}.\nNalezené výsledky: {book}"
            else:
                return f"Kniha nebyla nalezena."


# ad 2:


def film_searching_by_name(value):
    films_lst = []
    for film in films:
        if value in film["název"]:
            films_lst.append(film)
    if films_lst == {}:
        return f"Film nebyl nalezen"
    else:
        print_film(films_lst)


def print_film(film):
    for f in film:
        for key, value in f.items():
            print(f"{key}: {value}")
    print()


def add_film(name, director, year, actors):
    films.append(
        {"název": name, "režisér": director, "rok_vydání": year, "herci": actors}
    )


def update_film(idx, key, new_value):
    films[idx - 1][key] = new_value


def printing_films():
    for idx, film in enumerate(films):
        print(f"{idx + 1}: {film}")


# ad 3:


def add_employee():
    name = input("Name of employee: ")
    position = input("Position: ")
    salary = input("Salary: ")
    employees[name] = {"pozice": position, "plat": salary}


def del_employee():
    to_delete = input("Give me name of employee, you want to delete: ")
    del employees[to_delete]


def update_employee():
    name = input("Which employee you want to update: ")
    new_position = input("New position:")
    new_salary = input("New salary: ")
    employees.update({name: {"pozice": new_position, "salary": new_salary}})


def search_employee_by_position(position):
    names = []
    for name, value in employees.items():
        if position in value.values():
            names.append(name)
    return names


def search_employee_by_salary(salary):
    names = []
    for name, value in employees.items():
        if salary == value["plat"]:
            names.append(name)
    return names


def pr_empl():
    x = 1
    print()
    for employee, value in employees.items():
        print(f"{x}. {employee}: {value}")
        x += 1
    print()
