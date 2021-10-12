"""
Daniel Hoberman
HW5

Description:
Solving blockworld with depth search, bread search, and A*
"""


import random

class Blockworld():

    '''
    Initializes blockworld board with board rows and number of blocks
    '''
    def __init__(self, rows, blocks):
            self.rows = rows
            self.blocks = blocks
            board = [[] for bracket in range(self.rows)]
            rand_vals = random.sample(range(self.blocks), self.blocks)
            self.board_values = rand_vals
            for val in rand_vals:
                board[0].append(val)
            self.board = board

    '''
    Displays board using horizontal printing method
    '''
    def display_board(self):
        for row in self.board:
            line = "- "
            for piece in row:
                line += str(piece)
                line += " "
            print(line)

    
    '''
    Generate list of valid moves in binary format
    '''
    def check_valid_moves(self):
        valid_moves = []
        for locs in range(self.rows):
            if self.board[locs] == []:
                continue
            elif locs == 0:
                valid_moves.append([locs, 1])
            elif locs == self.rows - 1:
                valid_moves.append([locs, -1])
            else:
                valid_moves.append([locs, -1])
                valid_moves.append([locs, 1])
        return valid_moves

    '''
    Checks to see if game is over, done by seeing if column is sorted
    '''
    def is_done(self):
        for column in self.board:
            column_value = len(column) 
            if column_value == 0:
                continue

            if column_value == self.blocks:
                return all(column[i] <= column[i + 1] for i in range(len(column) - 1))


    '''
    Makes move using binary system
    '''
    def make_move(self, cur_col, new_col):
        move = cur_col + new_col
        num = self.board[cur_col].pop()
        self.board[move].append(num)


    '''
    For location in board changes to string format for better display
    '''
    def to_string(self):
        string = ""
        for loc in self.board:
            string += "|" + str(loc) + "\n"
        return string



    '''
    Checks to see if each state has repetition by checking inside each element in state
    '''
    def state_already_hit(self, prevStates):
        for state in prevStates:
            if self.compare_states(state) == True:
                return True
        return False


    '''
    compares current board with state board
    '''
    def compare_states(self, state):
        for i in range(self.rows):
            if len(self.board[i]) != len(state.board[i]):
                return False
            for j in range(len(self.board[i])):
                if self.board[i][j] != state.board[i][j]:
                    return False
        return True  
