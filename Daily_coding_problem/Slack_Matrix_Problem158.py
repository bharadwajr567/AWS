'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Slack.
You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?
You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.
For example, given the following matrix:
[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:
    Right, down, down, right
    Down, right, down, right
The top left corner and bottom right corner will always be 0.
'''

#implementation with importing libraries 

import numpy as np

matrice = np.array([[0, 0, 1],
                     [0, 0, 1],
                     [1, 0, 0]])
    

def number_path(matrice,pos=[0,0]):

    N,M=np.shape(matrice)
    if pos==[N-1,M-1]:
        return 1
    
    if matrice[pos[0],pos[1]]==1:
        return 0
    
    a=0
    b=0
    if pos[0]<N-1:
        a=number_path(matrice,[pos[0]+1,pos[1]])
    if pos[1]<M-1:
        b=number_path(matrice,[pos[0],pos[1]+1])
        
    return a+b

#method 2 - Pythonic way 

EMPTY = 0
WALL = 1

def num_ways(matrix):
    m, n = len(matrix), len(matrix[0])
    num_ways_matrix = [[0 for j in range(n)] for i in range(m)]

    # Fill first row
    for j in range(n):
        if matrix[0][j] == WALL:
            break
        num_ways_matrix[0][j] = 1

    # Fill first col
    for i in range(m):
        if matrix[i][0] == WALL:
            break
        num_ways_matrix[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            from_top = num_ways_matrix[i - 1][j] if matrix[i - 1][j] != WALL else 0
            from_left = num_ways_matrix[i][j - 1] if matrix[i][j - 1] != WALL else 0

            num_ways_matrix[i][j] = from_top + from_left

    return num_ways_matrix[m - 1][n - 1]
    

m = [[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
 
print(num_ways(m))

#o/p - 2