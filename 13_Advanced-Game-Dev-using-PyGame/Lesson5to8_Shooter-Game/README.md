# Instructions to create an executable file of the game (for M14L1)

1. In the terminal, `cd` into the folder containing the game script and assets.
2. Use the following command to create the executable (make sure `pyinstaller` is installed):

```bash
pyinstaller --onefile --noconsole --name ShooterGame \ 
    --add-data "galaxy.jpg;." --add-data "bullet.png;." \
    --add-data "rocket.png;." --add-data "ufo.png;." \
    --add-data "space.ogg;." --add-data "fire.ogg;." \ 
    shooter_game.py
```

3. An executable file will be created under `dist/` in the same folder as the game script and assets. Double-click on the executable file to run the game.