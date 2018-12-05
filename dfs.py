"""LIFO (Last In, First Out) is a stack where the most recent elements are the first ones to be removed from the stack. In the next cell you can see one of the many possible implementations of LIFO using lists. There are two main functions:

Push: responsable for inserting a new element on the correct position of the stack
Pop: responsable for removing the correct element from the stack"""

LIFO_list = list()

def LIFO_push(LIFO_list,element):
    LIFO_list.append(element)

def LIFO_pop(LIFO_list):
    return LIFO_list.pop(-1)


"""Depth-First Search (DFS)¶
Depth-First search is a traversal/search algorithm for trees and graphs 
that starts at a root vertex and explores as far as possible along each branch before backtracking.

Exercise A (1pt)
Complete the DFS function which performs a DFS over a graph using a LIFO stack. 
It receives are the maze map, which is a graph represented in a dictionary, in the 
same way we used in Lab 1 and a starting position. It should return a list with the order 
of executed notes and a dictionary containing the vertexs as the keys and its parents as the value. 
You should not visit the same vertex twice."""

def add_to_explored_vertices(explored_vertices,vertex):
    explored_vertices.append(vertex)

def is_explored(explored_vertices,vertex):
    return vertex in list(explored_vertices)
    
def DFS(maze_graph, initial_vertex) :
    
    # explored vertices list
    explored_vertices = list()
    
    #LIFO stack
    queuing_structure = list()
    
    #Parent Dictionary
    parent_dict = dict()
        

    LIFO_push(queuing_structure,(initial_vertex,None)) # push the initial vertex to the queuing_structure
    while len(queuing_structure) > 0: #   while queuing_structure is not empty:
        # current_vertex,parent = queuing_structure.pop()
        # if the current vertex is not explored
            # add current_vertex to explored vertices
            # use parent_dict to map the parent of the current vertex
            # for each neighbor of the current vertex in the maze graph:
                # if neighbor is not explored:
                    # push the tuple (neighbor,current_vertex) to the queuing_structure
        current_vertex,parent = LIFO_pop(queuing_structure) 
        #
        # YOUR CODE HERE
        #
        if not is_explored(explored_vertices, current_vertex):
            add_to_explored_vertices(explored_vertices, current_vertex)
            parent_dict[current_vertex] = parent
            for neighbor in maze_graph[current_vertex]:
                if not is_explored(explored_vertices, neighbor):
                    LIFO_push(queuing_structure,(neighbor,current_vertex))

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

#### To show the output of maze_graph
#print(maze_graph[(0,0)])
#for neighbor in maze_graph[(0,0)]:
#    print(neighbor)

explored_vertices,parent_dict = DFS(maze_graph, (0,0))

print("Explored vertices order: {}".format(explored_vertices))
for vertex,parent in sorted(parent_dict.items(),key=itemgetter(0,0)):
    print("Vertex {} is the parent of vertex {}".format(parent,vertex))