from arena import *

# setup library
arena = Arena("arena.andrew.cmu.edu", "realm", "example")

def main():
    # make a cube
    cube = Cube(object_id="my_cube", position=Position(0,4,-2), \
                scale=Scale(2,2,2))
    # add the cube
    arena.add_object(cube)

# add and start tasks
arena.run_once(main)
arena.run_tasks()
