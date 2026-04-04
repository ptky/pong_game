from pynput import keyboard
import os
import time
import random
pointer_index = 0
ball_index = 0
points = 0
lives = 3
run = True
game_over = False

def clear(mode):
     if mode == 1:
          os.system('cls' if os.name=='nt' else 'clear')
     elif mode == 2:
          os.system("clear")
     else:
          run = False
          print("Config error. Check config.ini file")
          exit(0)

def map_generate(size_x,size_y):
     map_data = {}
     for i in range(1,size_x*size_y+1):
          map_data[i] = " "
     return map_data,size_x,size_y

def render_map(map_data,size_x):
     for i in range(1,len(map_data)+1):
          x = (i-1) % size_x
          
          if x == 0 or x == (size_x - 1):
               data = "#"
          else:
               data = map_data[i]
          if i % size_x == 0:
               print(data)
          else:
               print(data,end="")

          
     return map_data
          
def render_pointer(map_data,size_x,size_y):
     total = size_x*size_y
     map_data[size_x*size_y-size_x+1+(size_x//2)+pointer_index] = "_"
     return map_data


def move(direction,map_data,size_x,size_y,mode):
     global pointer_index
     #if you are on windows you need this: clear()
     #if you are using mac os you need this: os.system("clear")
     map_data[size_x*size_y-size_x+1+(size_x//2)+pointer_index] = " "
     if direction == 1 and pointer_index > -(size_x//2 -1):
          pointer_index-=1
     elif direction == 2 and pointer_index < (size_x//2 -1):
          pointer_index+=1
     map_data = render_pointer(map_data, size_x, size_y)
     clear(mode=mode)
     render_map(map_data, size_x)

def delete_old_ball(map_data,size_x,size_y):
     for i in range(1, size_x*size_y+1):
            if map_data[i] == "O":
                map_data[i] = " "

def drop_ball(map_data,size_x,size_y,speed,mode):
     global ball_index
     global points
     global lives
     global run
     global game_over
     y = 0
     x_cord = random.randint(1,size_x-2)
     while run:
          if lives == 0 and not game_over:
               game_over = True
               keyboard_glitch = input("Press enter! ")
               clear(mode=mode)
               print("Game Over!\n")
               print(f"Your total score: {points}")
               qstn = int(input("Wanna retry? (1 = Yes, 2 = No): "))
               if qstn == 1:
                    lives = 3
                    game_over = False
                    points = 0
                    y = 0
                    continue
               elif qstn == 2:
                    print("Click a random button on your keyboard.")
                    run = False
                    return
                    
                    

          delete_old_ball(map_data=map_data,size_x=size_x,size_y=size_y)
          
          index = y * size_x + x_cord + 1
          #if you are on windows you need this: clear()
          #if you are using mac os you need this: os.system("clear")
          if y == size_y - 1:
            if map_data[index] == "_":
                points += 1
            elif map_data[index] == " ":
                 lives-=1
            y = 0
            x_cord = random.randint(1,size_x-2)

          else:
               y += 1

          map_data[index] = "O"
          render_pointer(map_data, size_x, size_y)

          clear(mode=mode)
          render_map(map_data, size_x)
          print(f"Points: {points}")
          print(f"Lives left: {lives}")

          time.sleep(speed)

     #alapvetoen szeretnem ugy megcsinalni, hogy folyamatosan esnek a labdak es a chatgpt-vel otleteltem,
     #hogyan lehetne ugy megcsinalni, hogy ne bugoljon szet a console es azt irta a threading modulelal megtudom oldani

def on_press(key,pointer,size_x,size_y,mode):
    global points,lives
    if not run:
        return False

    try:
        if key.char == "a":
             move(direction=1, map_data=pointer, size_x=size_x, size_y=size_y,mode=mode)
             print(f"Points: {points}")
             print(f"Lives left: {lives}")
        elif key.char == "d":
            move(direction=2, map_data=pointer, size_x=size_x, size_y=size_y,mode=mode)
            print(f"Points: {points}")
            print(f"Lives left: {lives}")
    except AttributeError:
        pass 

def on_release(key):
    if key == keyboard.Key.esc:
        return False