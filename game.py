from pynput import keyboard
import os
import time
import threading,random
pointer_index = 0
ball_index = 0
points = 0
lives = 3
clear = lambda: os.system('cls')
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
     #if you are on windows you need this: clear()
     #if you are using mac os you need this: os.system("clear")
     map_data[size_x*size_y-size_x+1+(size_x//2)+pointer_index] = " "
     if direction == 1 and pointer_index > -(size_x//2):
          pointer_index-=1
     elif direction == 2 and pointer_index < (size_x//2):
          pointer_index+=1
     map_data = render_pointer(map_data, size_x, size_y)
     clear()
     render_map(map_data, size_x, size_y)

def delete_old_ball(map_data):
     for i in range(1, size_x*size_y+1):
            if map_data[i] == "O":
                map_data[i] = " "

def drop_ball(map_data,size_x,size_y):
     global ball_index
     global points
     global lives
     y = 0
     x_cord = random.randint(0,size_x-1)
     while True:
          if lives == 0:
               time.sleep(0.3)
               clear()
               print("Game Over!\n")
               print(f"Your total score: {points}")
               qstn = int(input("Wanna retry? (1 = Yes, 2 = No): "))
               if qstn == 1:
                    lives = 3
                    continue
               elif qstn == 2:
                    exit(0)

          delete_old_ball(map_data=map_data)
          
          index = y * size_x + x_cord + 1
          #if you are on windows you need this: clear()
          #if you are using mac os you need this: os.system("clear")
          if y == size_y - 1:
            if map_data[index] == "_":
                points += 1
            elif map_data[index] == " ":
                 lives-=1
            y = 0
            x_cord = random.randint(0, size_x-1)

          else:
               y += 1

          map_data[index] = "O"

          clear()
          render_map(map_data, size_x, size_y)
          print(f"Points: {points}")
          print(f"Lives left: {lives}")

          time.sleep(0.3)

     #alapvetoen szeretnem ugy megcsinalni, hogy folyamatosan esnek a labdak es a chatgpt-vel otleteltem,
     #hogyan lehetne ugy megcsinalni, hogy ne bugoljon szet a console es azt irta a threading modulelal megtudom oldani
     
     

data, size_x, size_y = map_generate(15, 5) # páratlannak kell lennie az x-nek hogy legyen kozepe
pointer = render_pointer(data, size_x, size_y)
render_map(pointer, size_x, size_y)
ball_thread = threading.Thread(target=drop_ball, args=(pointer, size_x, size_y))
ball_thread.daemon = True 
ball_thread.start()

def on_press(key):
    global points,lives
    try:
        if key.char == "a":
             move(direction=1, map_data=pointer, size_x=size_x, size_y=size_y)
             print(f"Points: {points}")
             print(f"Lives left: {lives}")
        elif key.char == "d":
            move(direction=2, map_data=pointer, size_x=size_x, size_y=size_y)
            print(f"Points: {points}")
            print(f"Lives left: {lives}")
    except AttributeError:
        pass 

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()