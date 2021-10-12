"""
Daniel Hoberman
HW5

Description:
Solves blockworld with strange version of A*, depth search, and bread search.
"""

import copy
from collections import deque
from blockworld import Blockworld


'''
checks to see distance for lowest number to right most column
'''
def heuristic(blockworld_copy, block):
    weight = 0
    start = find_block(blockworld_copy.board, block)
    depth = start[1]
    distance = blockworld_copy.blocks - (start[0]+1)
    weight += depth + distance
    return weight

'''
finds column index, and stack index of block
'''
def find_block(board, block):
    for col,stack in enumerate(board):
        stack.reverse()
        for i, val in enumerate(stack):
            if val == block:
                return [col, i]



'''
Creates deepcopy of blockworld and checks each one for heuristic
'''
def a_star_search(blockworld):
    weight = 0
        
    valid_moves = blockworld.check_valid_moves()
    block_list = blockworld.board_values
    for move in valid_moves:
        blockworld_copy = copy.deepcopy(blockworld)
        blockworld_copy.make_move(move[0], move[1])
        smallest = 100
            
        for num in block_list:
            if num in blockworld.board[-1]:
                block_list.remove(num)
            

        for value in block_list:
            if value < smallest:
                smallest = value

        h_score_move = heuristic(blockworld_copy, smallest)
        weight = h_score_move  
        move.append(weight)
    return valid_moves



'''
Makes move with A* for value with lowest valid_move score
'''
def a_star_choose_move(blockworld, valid_moves):
        smallest = 100
        index = 0
        for i, value in enumerate(valid_moves):
                if value[2] < smallest:
                    smallest = value[2]
                    index = i
        
        move = valid_moves[index]
        blockworld.make_move(move[0], move[1])
        return None



'''
Runs A* until final state is found
'''
def call_a_star(blockworld = Blockworld(3,3)):

    print("A* search Start")
    print("_______________")
    
    while not blockworld.is_done():
        blockworld.display_board()
        valid_move = a_star_search(blockworld)
        a_star_choose_move(blockworld, valid_move)
        blockworld.display_board()
        print()

    if blockworld.is_done():
        print("A* solved")
        blockworld.display_board()



'''
Recursive depth_search algorithm keeps track of state
'''
def depth_search(blockworld = Blockworld(3,3), track_state = [], track_path = [], depth = 50):
    
    track_state.append(blockworld)
    track_path.append(blockworld)
    if blockworld.is_done():
        return True, track_path
    if depth == 0:
        return False, track_path

    for valid_move in blockworld.check_valid_moves():
        new_path = copy.deepcopy(blockworld)
        new_path.make_move(valid_move[0], valid_move[1])

        visited = False
        for val in track_state:
            if new_path == val:
                visited = True
                break

        if not visited:
            solved, newPath = depth_search(new_path, track_state, [val for val in track_path], depth - 1)
            if solved:
                return True, newPath
    
    return False, track_path
 

'''
starts the recursive algorithm for depth search
'''
def call_depth():
    print("Depth Search Start")
    print("__________________")
    value, path = depth_search()
    for val in path:
        val.display_board()
        print()

    print("Depth Search Solved")
    print()



'''
Recursive breadth search algorithm. Done using queue.
'''
def breadth_search(prevState, q):
    if not len(q):
        return False

    current_board = q.pop()
    prevState.append(current_board)
    if current_board.is_done():
        current_board.display_board()
        return current_board

    current_board.display_board()
    print()

    valid_moves = current_board.check_valid_moves()
    for move in valid_moves:
        child = copy.deepcopy(current_board)
        child.make_move(move[0], move[1])
    
        if (child.state_already_hit(prevState) == True):
            continue
        else:
            q.append(child)

    breadth_search(prevState, q)



'''
Creates queue, and adds first element. Calls breadth_search
'''
def call_breadth():
    print("Breadth Search Start")
    print("____________________")
    blockworld= Blockworld(3,3)
    q = deque()
    prevState = []
    q.append(blockworld)
    breadth_search(prevState, q)
    print("Bread Search Solved")
    print()

