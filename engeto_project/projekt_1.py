"""
projekt_1.py: prvni projekt do Engeto Online Python Akademie

author: Lizal Adam
email: lizaladam@seznam.cz
discord: Adam_L



"""

TEXTS = [
    """
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
    """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""",
]


min_pos = TEXTS.index(min(TEXTS)) + 1
max_pos = TEXTS.index(max(TEXTS)) + 1

number_of_texts = len(TEXTS)
registred_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}
line = "-" * 35


username = input("username: ")
password = input("password: ")
print(line)

if username in registred_users:
    print(f"Welcome to the app, {username}")
    print(f"We have {number_of_texts} texts to be analyzed.", line, sep="\n")

else:
    print("unregistred user, terminating the program...")
    quit()

enter_number = input(f" Enter a number btw. {min_pos} and {max_pos} to select:")
