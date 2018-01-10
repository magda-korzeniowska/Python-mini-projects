# Python mini-project no. 0 - Name Generator
# randomly generates male and female names from a given list of names and surnames

import random

female_name = ["Joanna", "Magdalena", "Matylda", "Jadwiga"]
male_name = ["Aleksander", "Michał", "Grzegorz", "Dominik"]

surname = ["Gajewski", "Nowak", "Nadworny", "Skowycki", "Myśliński", "Robak"]


while True:
    choice = input("to generate female name - press 'f', male name - press 'm', to quit press - 'q'")
    if choice in ("f", "m", "q"):
        if choice == "m":
            new_name = random.choice(male_name) + " " + random.choice(surname)
            print(new_name)
            break

        elif choice == "f":
            generated_surname = random.choice(surname)
            if generated_surname[-1] == "i":
                generated_surname = generated_surname.split()
                generated_surname = generated_surname[-1].replace("i", "a")
            new_name = random.choice(female_name) + " " + generated_surname
            print(new_name)
            break

        else:
            break

    else:
        print("You typed something wrong!")

