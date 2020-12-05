import requests
import json
import re
import io
from datetime import date

# environment variables
leaderboard = os.getenv('leaderboard')
session = os.getenv('session')
readme = os.getenv('file')
id = os.getenv('id')
day_regex = os.getenv('day_regex')
stars_regex = os.getenv('stars_regex')

# fetch stars
cookie = { 'session' : session }
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