import os
for file in os.listdir("/home/calebe945/PlayOnLinux's virtual drives/calebe945/drive_c/Program Files/Steam/steamapps/"):
    if file.endswith(".acf"):
        print("Steam_WINE:",file)

for file in os.listdir("/home/calebe945/.steam/steam/steamapps/"):
    if file.endswith(".acf"):
        print("Steam_NATIVE:",file)

