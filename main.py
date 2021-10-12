"""
Daniel Hoberman
HW5

Description:
Solves blockworld with strange version of A*, depth search, and bread search
"""


import algorithms
import sys

orig_stdout = sys.stdout
f = open('blockworld_algorithms_output.txt', 'w')
sys.stdout = f

algorithms.call_depth()
algorithms.call_breadth()
algorithms.call_a_star()

f.close()