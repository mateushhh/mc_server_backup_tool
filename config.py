SERVER_DIRECTORY = "F:/minecraft_server_test"
BACKUP_DIRECTORY = "F:/minecraft_server_backup"
SERVER_FILENAME = "fabric-server-mc.1.20.1-loader.0.18.4-launcher.1.1.1.jar"

"""
Default Value for maximum backup compatibility
If you have special mod configuration folders outside './mods' folder like ./squaremap 
You need to add it to DIRECTORIES_TO_BACKUP array below
"""
#SERVER_PERMISSIONS = ["banned-ips.json", "banned-players.json", "whitelist.json", "ops.json"]
#SERVER_CONFIGURATION = ["eula.txt", "server.properties", "start.bat"]

#DIRECTORIES_TO_BACKUP = ["world", "versions", "mods", "libraries", "config", ".fabric"]
#FILES_TO_BACKUP = [SERVER_FILENAME] + SERVER_CONFIGURATION

SERVER_PERMISSIONS = ["banned-ips.json", "banned-players.json", "whitelist.json", "ops.json", "usercache.json", "usernamecache.json"]
SERVER_CONFIGURATION = ["eula.txt", "server.properties", "start.bat", "server-icon.png"]

DIRECTORIES_TO_BACKUP = ["world", "versions", "squaremap", "skins", "mods", "libraries", "config", ".fabric"]
FILES_TO_BACKUP = [SERVER_FILENAME] + SERVER_CONFIGURATION
ROOT_FOLDER = "minecraft_server"