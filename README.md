# Sudoku-Solver-DFS-
A Python program that solves Sudoku puzzles using Depth-First Search (DFS) and backtracking.
# Algorithm Overview
The program applies DFS to explore all possible states of the Sudoku grid:
1. Find the first empty cell (represented by 0).
2. Try filling it with numbers from 1 to 9.
3. For each number, check if it’s valid according to Sudoku rules (row, column, and 3x3 subgrid).
4. If valid, move recursively to the next empty cell.
5. If no number fits, backtrack to the previous cell and try a different value.

When no empty cells remain, the puzzle is solved.
