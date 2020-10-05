import os
import glob
import json
import time
import datetime
import sav_to_json as sv

print()
print("Breath of the Wild Playtime")
print()

save_dir = "C:/Games/The Legend of Zelda - Breath of the Wild/cemu/mlc01/usr/save/00050000/101c9500/user/80000001"

# Using '*' pattern  
files = glob.glob(save_dir + '/**/game_data.sav', recursive=True) 

# Check for empty list.
if not files:
    print("Savegames not found.")
    exit()

# Last modified time
latest_file = max(files, key=os.path.getmtime)
print('Savegame: ' + latest_file) 

# convert to json
sv.convert_to_json(latest_file)

# Read playtime from json
with open('game_data.sav.json') as json_file:
    data = json.load(json_file)

playtime = data['PlayReport_PlayTime']

print("Your current playtime: " + str(datetime.timedelta(seconds=playtime)))
print()
time.sleep(3)
