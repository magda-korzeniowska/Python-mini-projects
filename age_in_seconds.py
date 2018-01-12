# Python mini-project no. 2 - Age in Seconds
# calculates your age in seconds based on your day of birth

from datetime import datetime

while True:
    user_input = input("Give me a date of your birth: (YYYY-MM-DD)")
    try:
        birth_date = datetime.strptime(user_input, "%Y-%m-%d")
    except Exception:
        print("Wrong date format!")
        continue

    now = datetime.now()
    delta = now - birth_date
    total_seconds = round(delta.total_seconds(),1)

    print("You are {} seconds old!".format(total_seconds))
    break




