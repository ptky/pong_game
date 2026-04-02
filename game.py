from pynput import keyboard
import os
import time
import threading,random
pointer_index = 0

def map_generate(size_x,size_y):
     map_data = {}
     for i in range(1,size_x*size_y+1):
          map_data[i] = " "
     return map_data,size_x,size_y

def render_map(map_data,size_x,size_y):
     for i in range(1,len(map_data)+1):
          if i % size_x == 0:
               print(map_data[i])
          else:
               print(map_data[i],end="")
     return map_data
          
def render_pointer(map_data,size_x,size_y):
     total = size_x*size_y
     map_data[size_x*size_y-size_x+1+(size_x//2)+pointer_index] = "_"
     return map_data


def move(direction,map_data,size_x,size_y):
     global pointer_index
     os.system("clear")
     map_data[size_x*size_y-size_x+1+(size_x//2)+pointer_index] = " "
     if direction == 1 and pointer_index > -(size_x//2):
          pointer_index-=1
     elif direction == 2 and pointer_index < (size_x//2):
          pointer_index+=1
     map_data = render_pointer(map_data, size_x, size_y)
     render_map(map_data, size_x, size_y)

def drop_ball(map_data,size_x,size_y):
     x_cord = random.randint(0,size_x)

     #alapvetoen szeretnem ugy megcsinalni, hogy folyamatosan esnek a labdak es a chatgpt-vel otleteltem,
     #hogyan lehetne ugy megcsinalni, hogy ne bugoljon szet a console es azt irta a threading modulelal megtudom oldani
     
     

data, size_x, size_y = map_generate(15, 5)
pointer = render_pointer(data, size_x, size_y)
render_map(pointer, size_x, size_y)
ball_thread = threading.Thread(target=drop_ball, args=(pointer, size_x, size_y))
ball_thread.daemon = True 
ball_thread.start()

def on_press(key):
    try:
        if key.char == "a":
             move(direction=1, map_data=pointer, size_x=size_x, size_y=size_y)
             print("Points: 0")
        elif key.char == "d":
            move(direction=2, map_data=pointer, size_x=size_x, size_y=size_y)
            print("Points: 0")
    except AttributeError:
        pass 

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()