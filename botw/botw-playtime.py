import os
import glob

save_dir = "C:/Games/The Legend of Zelda - Breath of the Wild/cemu/mlc01/usr/save/00050000/101c9500/user/80000001"

# Using '*' pattern  
print('Savegame:') 
files = glob.glob(save_dir + '/**/game_data.sav', recursive=True) 

# Check for empty list.
if not files:
    print("Not found")
    exit()

# Last modified time
latest_file = max(files, key=os.path.getmtime)
print(latest_file)