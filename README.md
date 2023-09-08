# 3x3-Sliding-Puzzle

A* search to solve a 3x3 sliding tile puzzle in the most efficient order

## Description

<table align="center">
<tr><th>Unsolved</th><th>Solved</th></tr>
<tr><td>

| 5 | 2 | 7 |
| --- | --- | --- |
|   | 1 | 3 |
| 6 | 8 | 3 |

</td><td>

| 1 | 2 | 3 |
| --- | --- | --- |
| 4 | 5 | 6 |
| 7 | 8 |   |

</td></tr> </table>

* Starting from a given 9-element array that has a value of 0-8 in each entry, where the value represents the tile in that location (0 represents the empty space).

* The locations in the array scan left to right, and then top to bottom, so for example, the state shown above on the left would be [5,2,7,0,1,4,6,8,3], and the goal state (shown above on the right) would be [1,2,3,4,5,6,7,8,0].

* The only actions available are to move the blank tile up, right, down, or left (represented by 0,1,2,3 respectively).

* The total (sum for all tiles, not including the empty tile) Manhattan distance between each tile location and its goal location is used as the admissible heuristic.

* The program returns the depth the solution was found, the number of nodes expanded (taken out of frontier), and the sequence of actions found. For example, the above puzzle returns depth = 23, nodes expanded = 687, and a sequence of [1, 1, 0, 3, 3, 2, 1, 2, 3, 0, 1, 1, 2, 3, 0, 3, 2, 1, 0, 0, 1, 2, 2]
