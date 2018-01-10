# Python mini-project no. 1 - Higher Lower
# number guessing game

#ver. 1

from random import randint
guessed = False
rnd = randint(1, 9)

while not guessed:
    str_num = input("Podaj liczbę od 1 do 9:")
    try:
        num = int(str_num)
        if num > 9:
            print("liczba musi być w zakresie 1-9!")
            continue
    except ValueError:
        print("Liczbę, było!")
        continue

    if num > rnd:
        print("Za dużo!")
    elif num < rnd:
        print("Za mało!")
    else:
        print("Brawo!")
        guessed = True



# ver. 2 with Flask

from random import randint
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/guess", methods=['GET', 'POST'])
def guess():
    html = """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
    {}
        <form method='POST'>
            Zgadnij liczbę:<br>
                <input type="text" name="guessed"><br>
                <input type="hidden" name="random" value="{}">
                <br>
                <button type="submit">Wyślij</button>
        </form>
    </body>
</html>
"""

    if request.method == 'GET':
        random = randint(1, 9)
        return html.format("", random)

    else:
        if request.form["guessed"] < request.form["random"]:
            msg = "Za mało"
        elif request.form["guessed"] > request.form["random"]:
            msg = "Za dużo"
        else:
            msg = "Zgadłeś!"
        return html.format(msg, request.form["random"])


if __name__ == "__main__":
    app.run()

