import datetime
import zipfile
import os
import config

DATETIME_STR = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
BACKUP_PATH = config.BACKUP_DIRECTORY + "/" + DATETIME_STR + "_backup.zip"

progress_bar = 0
progress_bar_max = len(config.DIRECTORIES_TO_BACKUP) + len(config.FILES_TO_BACKUP)

def print_progress(filename):
    global progress_bar, progress_bar_max
    progress_bar += 1
    print("(" + str(round(progress_bar / progress_bar_max * 100,1)) + "%)\t'" + filename + "' added to the backup")

try:
    print("Creating backup file")
    backup = zipfile.ZipFile(BACKUP_PATH, mode="w", compression=zipfile.ZIP_STORED)

    for file in config.FILES_TO_BACKUP:
        backup.write(config.SERVER_DIRECTORY+"/"+file, config.ROOT_FOLDER+"/"+file)
        print_progress(file)

    for directory in config.DIRECTORIES_TO_BACKUP:
        source_dir = os.path.join(config.SERVER_DIRECTORY, directory)

        for root, dirs, files in os.walk(source_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, config.SERVER_DIRECTORY)
                zip_path = os.path.join(config.ROOT_FOLDER, rel_path)

                backup.write(full_path, zip_path)
        print_progress(directory)

    print("Backup complete \"" + BACKUP_PATH + "\" created")
except Exception as e:
    print("Something went wrong: " + str(e))
