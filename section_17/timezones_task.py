import pytz
from datetime import datetime

format = "%Y-%m-%d %H:%M:%S %Z%z"

print("""AE United Arab Emirates ['Asia/Dubai']
AF Afghanistan ['Asia/Kabul']
""")

user_tz = input("Pleas enter a two-letter code of the country\n"
                "to choose the time zone or 'q' to quite : ")
dictinori = {
    "AE": 'Asia/Dubai',
    "AF": 'Asia/Dubai',
}
while user_tz != "q":
    time = datetime.now(pytz.timezone(dictinori[user_tz]))
    print(time.strftime(format))

    now_utc = datetime.now(pytz.timezone('UTC'))
    print(now_utc.strftime(format))

    user_tz = input()
