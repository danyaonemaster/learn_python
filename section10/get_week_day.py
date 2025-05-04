def get_week_day():
    week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    index = 0

    while index <= 6:
        yield week_days[index]
        index += 1

current_day = get_week_day()

for week_day in current_day:
    print(week_day)
