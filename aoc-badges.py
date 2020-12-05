import requests
import json
import os
import re
import io
from datetime import date

# environment variables
leaderboard = os.getenv('INPUT_LEADERBOARD')
session = os.getenv('INPUT_SESSION')
readme = os.getenv('INPUT_FILE')
id = os.getenv('INPUT_USERID')
day_regex = os.getenv('INPUT_DAYREGEX')
stars_regex = os.getenv('INPUT_STARSREGEX')
if leaderboard is None or leaderboard == 'None' :
  leaderboard = 'https://adventofcode.com/2020/leaderboard/private/view/' + id + ".json"

# fetch stars
cookie = { 'session' : session }
print('Fetching leaderboard data from : ' + leaderboard)
r = requests.get(leaderboard, cookies = cookie)
print(r.text)
data = json.loads(r.text)
stars = data['members']['658601']['stars']

# current day
today = date.today()
day = today.day if today.month == 12 else 24

print('Day: ' + str(day))
print('Stars: ' + str(stars))

# read file
f = io.open(readme, mode='r', encoding='utf-8')
txt = f.read()
f.close()

#replace values
txt = re.sub(day_regex, str(day), txt)
txt = re.sub(stars_regex, str(stars), txt)

# write back file
f = io.open(readme, mode='w', encoding='utf-8')
f.write(txt)
f.close()
