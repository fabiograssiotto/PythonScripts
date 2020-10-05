import os
import glob
import json
import time
import datetime
import sav_to_json as sv

#save_dir = "C:/Games/The Legend of Zelda - Breath of the Wild/cemu/mlc01/usr/save/00050000/101c9500/user/80000001"
save_dir = "C:/tmp"

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

print("Your current Botw playtime: " + str(datetime.timedelta(seconds=playtime)))
time.sleep(3)
print("Bye")
