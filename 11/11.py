"""Brute force solution for project-euler problem 11"""
import json
import os.path
from operator import mul

grid_file = os.path.join(os.path.dirname(__file__), 'grid.json')
grid = json.load(open(grid_file))

answer = 0
for row, col in ((x, y) for y in xrange(0, 20) for x in xrange(0, 20)):
    # Horizontal
    if col < 16:
        prod = reduce(mul, grid[row][col:col+4])
        answer = max(prod, answer)
    # Vertical
    if row < 16:
        prod = reduce(mul, (grid[r][col] for r in xrange(row, row+4)))
        answer = max(prod, answer)
    # Diagonal-right
    if col < 16 and row < 16:
        prod = reduce(mul, [grid[c+row][c+col] for c in xrange(4)])
        answer = max(prod, answer)
    # Diagonal-left
    if row > 4 and col > 4:
        prod = reduce(mul, [grid[19-row+c][19-col-c] for c in xrange(4)])
        answer = max(prod, answer)

print "Problem 11 Answer:", answer
