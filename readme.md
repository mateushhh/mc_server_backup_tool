# Minecraft Server Backup Tool (Fabric)

### How to use:
- Clone the repository so that the project folder is at the same depth level as your Minecraft server folder
- Set up `SERVER_DIRECTORY`, `BACKUP_DIRECTORY` and `SERVER_FILENAME` in `config.py`
- Run main.py with python

### How to make it run automatically with each session end
- After setting it up, modify your `start.bat` file by adding:
```bat
python ../mc_server_backup_tool/main.py
```
- Your `start.bat` should look like this
```bat
@echo off
java -Xmx8G -Xms8G -jar fabric-server-mc.1.20.1-loader.0.18.4-launcher.1.1.1.jar nogui
python ../mc_server_backup_tool/main.py
pause
```

### TODO:
- Make better config with presets for backups (choosing how many files to backup)
- Add a progress bar