import game
import configparser
from pynput import keyboard
import threading
import time

config = configparser.ConfigParser()
config.read("config.ini")

MAP_WIDTH = int(config["GAME"]["MAP_WIDTH"])
MAP_HEIGHT = int(config["GAME"]["MAP_HEIGHT"])
BALL_SPEED = float(config["GAME"]["BALL_SPEED"])
OS_MODE = int(config["GAME"]["OS_MODE"])

start = input("Would you like to start the game? Y/N: ")
if start.lower() == "y":
     
    data, size_x, size_y = game.map_generate(MAP_WIDTH, MAP_HEIGHT)
    pointer = game.render_pointer(data, size_x, size_y)

    game.render_map(pointer, size_x)
    
    print("\n\t3",flush=True)
    time.sleep(0.75)
    print("\t2",flush=True)
    time.sleep(0.75)
    print("\t1",flush=True)
    time.sleep(0.75)

    ball_thread = threading.Thread(
            target=game.drop_ball,
            args=(pointer, size_x, size_y, BALL_SPEED, OS_MODE)
    )
    ball_thread.start()

    def on_press(key):
        
        return game.on_press(key, pointer, size_x, size_y, OS_MODE)

    with keyboard.Listener(on_press=on_press,on_release=game.on_release) as listener:
        listener.join()                             
else:
    exit(0)





