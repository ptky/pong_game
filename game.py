def map_generate(size_x,size_y):
     map_data = {}
     for i in range(1,size*size+1):
          map_data[i] = "-"
     return map_data,size

def render_map(map_data,size):
     for i in range(1,len(map_data)+1):
          if i % size == 0:
               print(map_data[i])
          else:
               print(map_data[i],end="")
     return map_data
          
def render_pointer(map_data,size):
     total = size*size
     map_data[size*size-size+1+(size//2)] = "_"
     return map_data


data,size = map_generate(5)
print(data)
rendered_info = render_map(data,size)
pointer = render_pointer(map_data=rendered_info,size=size)
render_map(pointer,size=size)
