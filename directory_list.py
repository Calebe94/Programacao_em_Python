import os
STEAM_LINUX = "/home/calebe945/PlayOnLinux's virtual drives/calebe945/drive_c/Program Files/Steam/steamapps/"
STEAM_WINE = "/home/calebe945/.steam/steam/steamapps/"
def getAppID(str):
	str1 = str.split('_')
	str2 = str1[1]
	str3 = str2.split('.')
	return str3[0]

for file in os.listdir(STEAM_LINUX):
	if file.endswith(".acf"):
		#arquivo = "%s%s" % (STEAM_LINUX,file)
		string = getAppID(file)
		print("STEAM_WINE:",file)
		print(string)

for file in os.listdir(STEAM_WINE):
	if file.endswith(".acf"):
		print("Steam_NATIVE:",file)
		print(getAppID(file))

