import requests
import json
import sys
from datetime import datetime
from datetime import time
from datetime import timedelta
from typing import NamedTuple

class Position(NamedTuple):
  latitude : str
  longitude : str

def getISSTimeAndPosition():
  response = requests.get("http://api.open-notify.org/iss-now.json")
  jsonObj = json.loads(response.content)
  current_time = datetime.fromtimestamp(jsonObj['timestamp']),
  position = Position(*(jsonObj['iss_position'].values()))
  return (current_time, position)

def print_values(time_value, position_value):
  sys.stdout.write(f"{str(*time_value)} : {str(position_value)}\r")
  sys.stdout.flush()


future_time = datetime.now() + timedelta(seconds=1)
print()
while True:
  if datetime.now() >= future_time:
    print_values(*getISSTimeAndPosition())
    t1 = datetime.now() + timedelta(seconds=1)




