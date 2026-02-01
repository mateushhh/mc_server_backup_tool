import shutil
import datetime

DATETIME_STR = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

SERVER_DIRECTORY = "F:/minecraft_server"
BACKUP_DIRECTORY = "F:/minecraft_server_backup"
BACKUP_PATH = BACKUP_DIRECTORY + "/" + DATETIME_STR + "_backup"

print("Creating backup")
shutil.make_archive(BACKUP_PATH, "zip", SERVER_DIRECTORY)
try:
    shutil.make_archive(BACKUP_PATH, "zip", SERVER_DIRECTORY)
    print("Backup complete \"" + BACKUP_PATH + "\" created")
except Exception as e:
    print("Something went wrong: " + str(e))
