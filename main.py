import game
import configparser
from pynput import keyboard
import threading

config = configparser.ConfigParser()
config.read("config.ini")

MAP_WIDTH = int(config["GAME"]["MAP_WIDTH"])
MAP_HEIGHT = int(config["GAME"]["MAP_HEIGHT"])
BALL_SPEED = float(config["GAME"]["BALL_SPEED"])
OS_MODE = int(config["GAME"]["OS_MODE"])

data, size_x, size_y = game.map_generate(MAP_WIDTH, MAP_HEIGHT)
pointer = game.render_pointer(data, size_x, size_y)

game.render_map(pointer, size_x, size_y)

ball_thread = threading.Thread(
    target=game.drop_ball,
    args=(pointer, size_x, size_y, BALL_SPEED, OS_MODE)
)
ball_thread.daemon = True
ball_thread.start()

def on_press(key):
    game.on_press(key, pointer, size_x, size_y,OS_MODE)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()