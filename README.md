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
# How to Run
1. Clone the repository  
git clone https://github.com/AnTsich/Sudoku-Solver-DFS-.git  
2. Navigate into the project folder  
cd Sudoku-DFS-Solver  
3. Run the program  
python sudoku-solver.py  

Alternatively, you can simply download the sudoku-solver.py file and run it directly with Python

# Example Input:
Copy and paste these 9 lines when the program asks for Sudoku input.  

9 8 0 0 0 0 0 0 2  
0 0 0 0 5 0 0 0 7  
7 0 3 0 0 0 9 0 0  
4 7 0 0 3 0 0 1 0  
0 2 0 1 4 7 0 9 0  
0 5 0 0 6 0 0 8 4  
0 0 7 0 0 0 3 0 1  
8 0 0 0 9 0 0 0 0  
5 0 0 0 0 0 0 2 9

# Author:
Created by [@AnTsich](https://github.com/AnTsich)  
Mathematics student with an interest in algorithms, problem solving, and Python programming.
