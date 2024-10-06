import datetime

now = datetime.datetime.now()
last_day = datetime.datetime(now.year, now.month + 1, 1) - datetime.timedelta(days = 1)
remaining_days = (last_day - now).days + 1

print(remaining_days + 1)

print(f"Remaining days in {now.strftime('%B %Y')}: {remaining_days} days")