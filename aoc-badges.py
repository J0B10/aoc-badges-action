import requests
import json
import os
import re
import io
from datetime import date, timedelta, datetime
import pytz

# environment variables
years_array = os.getenv('INPUT_YEAR')
leaderboard = os.getenv('INPUT_LEADERBOARD')
session = os.getenv('INPUT_SESSION')
readme = os.getenv('INPUT_FILE')
userid = os.getenv('INPUT_USERID')
day_regex = os.getenv('INPUT_DAYREGEX')
stars_regex = os.getenv('INPUT_STARSREGEX')
days_completed_regex = os.getenv('INPUT_DAYSCOMPLETEDREGEX')
if years_array is None or not years_array:
    years = date.today().year
else:
    try:
        years = list(map(int,years_array.split(',')))
    except ValueError:
        print('year input is not an integer')
        exit(1)

stars = 0
days_completed = 0
for year in years:
    if leaderboard is None or not leaderboard:
        leaderboard = f'https://adventofcode.com/{year}/leaderboard/private/view/{userid}.json'

    # fetch stars
    cookie = {'session': session}
    print('Fetching leaderboard data from : ' + leaderboard)
    r = requests.get(leaderboard, cookies=cookie)
    if r.status_code != 200:
        print(f'Leaderboard API returned status code {r.status_code}: {r.text}')
        exit(1)
    try:
        data = json.loads(r.text)
    except json.JSONDecodeError as err:
        print('Could not parse leaderboard json. Is the leaderboard url correct & your session code valid?')
        print(err)
        exit(1)
    # noinspection PyUnboundLocalVariable
    stars += data['members'][userid]['stars']

    # completed days
    for day in data['members'][userid]['completion_day_level']:
        if '2' in data['members'][userid]['completion_day_level'][day]:
            days_completed += 1

    # Set the timezone to New York
    new_york_tz = pytz.timezone('America/New_York')

    # Get the current time in New York
    today = datetime.now(new_york_tz).date()

    # Your existing logic to determine the day
    if today < datetime(year, 12, 1, tzinfo=new_york_tz).date():
        day = 0
    elif today > datetime(year, 12, 31, tzinfo=new_york_tz).date():
        day = 24
    else:
        day = today.day

    # Reset the leaderboard for the next year iteration
    leaderboard = None

print(f'Day: {day}')
print(f'Stars: {stars}')
print(f'Days completed: {days_completed}')

# read file
f = io.open(readme, mode='r', encoding='utf-8')
txt = f.read()
f.close()

# replace values
txt = re.sub(day_regex, str(day), txt)
txt = re.sub(stars_regex, str(stars), txt)
txt = re.sub(days_completed_regex, str(days_completed), txt)

# write back file
f = io.open(readme, mode='w', encoding='utf-8')
f.write(txt)
f.close()
