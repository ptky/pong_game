import keyboard,time
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
     map_data[size_x*size_y-size_x+1+(size_x//2)] = "_"
     return map_data

def move_pointer(map_data,size_x,size_y):
     pointer_pos = size_x*size_y-size_x+1+(size_x//2)
     for i in range(size_x*size_y-size_x+1, size_x*size_y+1):
        map_data[i] = " "
     if keyboard.is_pressed("d") and pointer_pos < size_x*size_y:
          pointer_pos += 1
     elif keyboard.is_pressed("a") and pointer_pos > size_x*size_y-size_x+1:
          pointer_pos -= 1

     map_data[pointer_pos] = "_"
     return map_data, pointer_pos

data,size_x,size_y = map_generate(15,5)
print(data)
rendered_info = render_map(data,size_x,size_y)
pointer = render_pointer(map_data=rendered_info,size_x=size_x,size_y=size_y)
render_map(pointer,size_x=size_x,size_y=size_y)
while True:
    moved,changed = move_pointer(map_data=pointer, size_x=size_x, size_y=size_y)
    if changed:
     render_map(moved, size_x,size_y)
     time.sleep(0.1)
