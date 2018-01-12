# Python mini-project no. 3 - Temperature Converter
# converts temperature from Fahrenheit to Celsius or vice-versa

# ver. 1

def convert(temp, unit):
    unit = unit.lower()
    if unit == "c":
        temp = round(((temp - 32) / 9.0 * 5.0) , 1)
        return "{} degrees Fahrenheit".format(temp)
    elif unit == "f":
        temp = round(((temp - 32) / 9.0 * 5.0), 1)
        return "{} degrees Celsius".format(temp)

# print("25 degrees Celsius =", convert(25, "c"))
# print("25 degrees Fahrenheit =", convert(25, "F"))


# ver. 2 with Flask

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/temperature", methods=['GET', 'POST'])
def convert():
    html = """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <form method='POST'>
            <h2>TEMPERATURE CONVERTER:</h2><br>
            Enter a temperature to convert:<br><br>
            <input name="temp">
            º
            <select name="unit">
                <option value="c">C</option>
                <option value="f">F</option>
            </select>
            <br>
            <button type="submit">CONVERT</button>
        </form>
    </body>
</html>
"""

    if request.method == 'GET':
        return html
    else:
        try:
            temp = float(request.form["temp"])
        except ValueError:
            return "Wrong data!"

        if request.form["unit"] == "c":
            new_temp = round((temp * 9.0 / 5.0 + 32), 1)
            return "{}º Celsius = {}º Fahrenheit".format(request.form["temp"], str(new_temp))
        elif request.form["unit"] == "f":
            new_temp = round(((temp - 32) / 9.0 * 5.0) , 1)
            return "{}º Fahrenheit = {}º Celsius".format(request.form["temp"], str(new_temp))

if __name__ == "__main__":
    app.run()