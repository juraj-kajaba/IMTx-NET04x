"""FIFO queue
FIFO (First In, First Out) is a queue where the oldest elements of the queue are the first ones to be removed. 
This type of queue has various applications including the Breadth-First search that we will code next.

Exercise B (1pt)
Based on the LIFO stack that we defined at the start of this session, create the auxiliary functions 
push and pop for a FIFO (first in first out) queue
"""

from utils import get_position_above,get_position_left,get_position_below,get_position_right
from utils import MOVE_UP,MOVE_DOWN,MOVE_LEFT,MOVE_RIGHT


FIFO_list = list()

def FIFO_push(FIFO_list,element):
    #
    # YOUR CODE HERE
    #
    FIFO_list.append(element)


def FIFO_pop(FIFO_list):
    #
    # YOUR CODE HERE
    #
    return FIFO_list.pop(0)


"""Breadth-first search (BFS)
Breadth-First search is another traversal/search algorithm for trees and graphs 
that unlike DFS tries to explore all the vertices at the present "depth" before going deeper 
in the data structure.

Exercise C (1pt)
Complete the BFS function which performs a BFS over a graph using a FIFO queue. 
As an input it receives the maze map that is a graph represented in a dictionary, 
in the same way we used in Lab 1 and a starting position. It should return a list 
with the order of executed vertices and a dictionary containing the vertices as the keys 
and its parents as the value. You should not visit the same vertex twice.
"""

def add_to_explored_vertices(explored_vertices,vertex):
    explored_vertices.append(vertex)

def is_explored(explored_vertices,vertex):
    return vertex in list(explored_vertices)


def BFS(maze_graph, initial_vertex, target_vertex = None) :
    
    # explored vertices list
    explored_vertices = list()
    
    #LIFO stack
    queuing_structure = list()
    
    #Parent Dictionary
    parent_dict = dict()
        

    FIFO_push(queuing_structure,(initial_vertex,None)) # push the initial vertex to the queuing_structure
    while len(queuing_structure) > 0: #   while queuing_structure is not empty:
        # current_vertex,parent = queuing_structure.pop()
        # if the current vertex is not explored
            # add current_vertex to explored vertices
            # use parent_dict to map the parent of the current vertex
            # for each neighbor of the current vertex in the maze graph:
                # if neighbor is not explored:
                    # push the tuple (neighbor,current_vertex) to the queuing_structure
        current_vertex,parent = FIFO_pop(queuing_structure)
        #
        # YOUR CODE HERE
        #
        if not is_explored(explored_vertices, current_vertex):
            add_to_explored_vertices(explored_vertices, current_vertex)
            parent_dict[current_vertex] = parent

            # Break the while loop if current vertex is target vertex
            if current_vertex == target_vertex:
                break

            for neighbor in maze_graph[current_vertex]:
                if not is_explored(explored_vertices, neighbor):
                    FIFO_push(queuing_structure,(neighbor,current_vertex))

    return explored_vertices,parent_dict 

from operator import itemgetter

#
# AUTOGRADER TEST - DO NOT REMOVE
#

maze_graph = {
    (0,0): {(0,1):1,(1,0):1}, 
    (0,1): {(0,2):1,(0,0):1},
    (1,0): {(1,1):1,(0,0):1},
    (1,1): {(1,2):1,(1,0):1},
    (0,2): {(0,1):1,(1,2):1},
    (1,2): {(0,2):1,(1,1):1}
}

explored_vertices,parent_dict = BFS(maze_graph, (0,0), (0,2))
print("explored vertices order: {}".format(explored_vertices))
for vertex,parent in sorted(parent_dict.items(),key=itemgetter(0,0)):
    print("vertex {} is the parent of vertex {}".format(parent,vertex))    

print(parent_dict)

"""Exercise D (1pt)
Using the parent_dictionary generated by running one of the searches, 
complete the function create_walk_from_parents, which receives the parent dictionary as input, 
an initial vertex and an target vertex. It returns a list which contains a walk between two points.    
"""



def create_walk_from_parents(parent_dict,initial_vertex,target_vertex):
    #
    # YOUR CODE HERE
    #
    retVal = []
    
    # Start with target_vertex
    current_vertex = target_vertex

    # Stop if initial_vertex is found
    while (current_vertex != initial_vertex):
        retVal.append(current_vertex)
        current_vertex = parent_dict[current_vertex]    
    
    # Return reversed list as we started from target
    retVal.reverse()
    
    return retVal


#
# AUTOGRADER TEST - DO NOT REMOVE
#

initial_vertex = (0,0)
target_vertex = (0,0)
explored_vertices,parent_dict = BFS(maze_graph,initial_vertex)
route = create_walk_from_parents(parent_dict,initial_vertex,target_vertex)
print("The route to go from vertex {} to {} is: {}".format(initial_vertex,target_vertex,route))


initial_vertex = (0,0)
target_vertex = (0,2)
explored_vertices,parent_dict = BFS(maze_graph,initial_vertex)
route = create_walk_from_parents(parent_dict,initial_vertex,target_vertex)
print("The route to go from vertex {} to {} is: {}".format(initial_vertex,target_vertex,route))    


def get_direction(initial_vertex,target_vertex):
    if get_position_above(initial_vertex) == target_vertex:
        return MOVE_UP
    elif get_position_below(initial_vertex) == target_vertex:
        return MOVE_DOWN
    elif get_position_left(initial_vertex) == target_vertex:
        return MOVE_LEFT
    elif get_position_right(initial_vertex) == target_vertex:
        return MOVE_RIGHT
    else:
        print("ddd init: " + str(initial_vertex) + " : " + str(target_vertex))
        raise Exception("vertices are not connected")

def walk_to_route(walk,initial_vertex):
    #
    # YOUR CODE HERE
    #
    retVal = []
    prev_vertex = initial_vertex

    for current_vertex in walk:
        # Skip first vertex if it is initial vertex
        if current_vertex != initial_vertex:
            retVal.append(get_direction(prev_vertex,current_vertex))
            prev_vertex = current_vertex

    return retVal
#
# AUTOGRADER TEST - DO NOT REMOVE
#


walk = [(0, 1), (1, 1), (2, 1)]
print("The route to walk {} is {}".format(walk,walk_to_route(walk,(0,0))))


def A_to_B(maze_graph,initial_vertex,target_vertex):
    #
    # YOUR CODE HERE
    #
    walk, parent_dict = BFS(maze_graph, initial_vertex, target_vertex)

    walk_from_par = create_walk_from_parents(parent_dict, initial_vertex, target_vertex)

    return walk_to_route(walk_from_par, initial_vertex)

#
# AUTOGRADER TEST - DO NOT REMOVE
#
a = (0,0)
b = (1,2)
print("The route from {} to {} is {}".format(a,b,A_to_B(maze_graph,a,b)))
print("The route from {} to {} is {}".format(b,a,A_to_B(maze_graph,b,a)))


import pyrat
pyrat.start_display()

starting_vertex = (2,2)
target_vertex = (4,4)

def turn(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese, timeAllowed):    
    return A_to_B(maze_graph=mazeMap,initial_vertex=playerLocation,target_vertex=piecesOfCheese[0])[0]


game = pyrat.Game(turn_1=turn,player1_start=starting_vertex,cheeses_start=[target_vertex])
game.play_match()
pyrat.display_game(game)