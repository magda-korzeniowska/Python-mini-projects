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

    print("You are {} seconds old!".format(str(total_seconds)))
    break


