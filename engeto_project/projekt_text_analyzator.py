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

if username in registred_users and registred_users[username] == password:
    print(f"Welcome to the app, {username}")
    print(f"We have {number_of_texts} texts to be analyzed.", line, sep="\n")

else:
    print("unregistred user, terminating the program...")
    quit()


try:
    enter_number = int(
        input(f" Enter a number btw. {min_pos} and {max_pos} to select: ")
    )
    print(line)

    num_words = []
    num_words_title = []
    num_words_upper = []
    num_words_lower = []
    num_words_numeric = []

    occur_words = {}

    if enter_number >= min_pos and enter_number <= max_pos:
        numberoftexts = TEXTS[enter_number - 1]
        for text in numberoftexts.split():
            clean_text = text.strip("-,.:;'")
            num_words.append(clean_text)
            if clean_text.istitle():
                num_words_title.append(clean_text)
            if clean_text.isupper():
                num_words_upper.append(clean_text)
            if clean_text.islower():
                num_words_lower.append(clean_text)
            if clean_text.isnumeric():
                num_words_numeric.append(int(clean_text))
        for word in num_words:
            word = len(word)
            if word not in occur_words:
                occur_words[word] = 1
            else:
                occur_words[word] += 1

        print(f"There are {len(num_words)} words in the selected text.")
        print(f"There are {len(num_words_title)} titlecase words.")
        print(f"There are {len(num_words_upper)} uppercase words.")
        print(f"There are {len(num_words_lower)} lowercase words.")
        print(f"There are {len(num_words_numeric)} numeric strings.")
        print(f"The sum of all the numbers {sum(num_words_numeric)}.")

        print(f"{line} \n LEN | OCCURENCES |NR. \n {line}")

        for key, value in sorted(occur_words.items()):
            char_len_word = "*" * value
            print(f" {key: <2} | {char_len_word: ^15} | {value} ")
    elif enter_number > number_of_texts:
        print(f"We don't have this number of text")
        quit()

except ValueError:
    print("Ooooops!! You have to choose a number")
