import copy

#Manhattan calculator
def manhattan(board):
    distance = 0
    coords = [(0,0), (0,1), (0,2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for l in range(len(board)):
        if board[l] != 0:
            distance += abs(coords[board[l] - 1][0] - coords[l][0]) + abs(coords[board[l] - 1][1] - coords[l][1])
    return distance

#tie
def compute_tie(i, curr_i, b_i, b_ci):
    x = ''.join([str(n) for n in b_i])
    y = ''.join([str(n) for n in b_ci])

    if int(x) > int(y):
        return i
    return curr_i

def move(board, action):
    coords = [(0,0), (0,1), (0,2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    #find 0 index
    zero_index = None
    for i in range(len(board)):
        if board[i] == 0:
            zero_index = i
            break
    
    #which action to take?
    zero_coords = coords[zero_index]
    swap_index = None
    swap_coords = None
    if action == 0 and zero_coords[0] - 1 >= 0:
        swap_coords = (zero_coords[0] - 1, zero_coords[1])
    elif action == 1 and zero_coords[1] + 1 <= 2:
        swap_coords = (zero_coords[0], zero_coords[1] + 1)
    elif action == 2 and zero_coords[0] + 1 <= 2:
        swap_coords = (zero_coords[0] + 1, zero_coords[1])
    elif action == 3 and zero_coords[1] - 1 >= 0:
        swap_coords = (zero_coords[0], zero_coords[1] - 1)
    
    #find swap index
    for i in range(len(coords)):
        if coords[i] == swap_coords:
            swap_index = i
            break
    
    if swap_coords != None:
        #return the board!
        new_board = copy.copy(board)
        new_board[swap_index] = board[zero_index]
        new_board[zero_index] = board[swap_index]
        return new_board
    return 0

#astar search
def astar(board):
    expanded = [] #keep track of expanded boards (board[10])
    path_frontier = [] #path of actions for each board (eg. [1, 1, 0, 3, 3, 2, 1, 2, 3, 0])
    frontier = [] # boards in the frontier (board[10])
    depth = [] #depth for each board (int)
    heuristic = [] #manhattan dist for each board h(n) (int)

    #ADDING THE ROOT
    frontier.append(board)
    depth.append(0)
    path_frontier.append([])
    heuristic.append(manhattan(board))
    steps = 0

    #BIG BOY LOOP
    while(frontier):
        steps = steps + 1
        #FIND BEST NODE
        min_f = 2**64
        curr_i = None
        for i in range(len(frontier)):
            f = depth[i] + heuristic[i]
            if f == min_f:
                curr_i = compute_tie(i, curr_i, frontier[i], frontier[curr_i])
            elif f < min_f:
                min_f = f
                curr_i = i

        #EXIT   
        if heuristic[curr_i] == 0:
            return depth[curr_i], steps, path_frontier[curr_i]
        
        #EXPAND FRONTIER
        curr_b = copy.copy(frontier[curr_i])
        #for all children c of i, reached with a
        for a in range(4):
            new_b = move(curr_b, a)
            
            #if action is valid
            if new_b != 0: 
                #check if new_b has already been expanded
                flag = False
                for b in expanded:
                    if new_b == b:
                        flag = True
                #if it hasn't, expand!
                if not flag:
                    frontier.append(new_b)
                    depth.append(depth[curr_i] + 1)
                    new_path = copy.copy(path_frontier[curr_i])
                    new_path.append(a)
                    path_frontier.append(new_path)
                    heuristic.append(manhattan(new_b))


        #FINISH
        expanded.append(curr_b)
        frontier.pop(curr_i)
        depth.pop(curr_i)
        path_frontier.pop(curr_i)
        heuristic.pop(curr_i)
        
        #remove other boards that equal curr_b
        for b in reversed(range(len(frontier))):
            if frontier[b] == curr_b:
                frontier.pop(b)
                depth.pop(b)
                path_frontier.pop(b)
                heuristic.pop(b)




#graphic print of board, feel free to use, or not
def print_board(board):
    print("\n")
    print("------------")
    print(
        "{:02d}".format(board[0]),
        "|",
        "{:02d}".format(board[1]),
        "|",
        "{:02d}".format(board[2]),
    )
    print("------------")

    print(
        "{:02d}".format(board[3]),
        "|",
        "{:02d}".format(board[4]),
        "|",
        "{:02d}".format(board[5]),
    )
    print("------------")

    print(
        "{:02d}".format(board[6]),
        "|",
        "{:02d}".format(board[7]),
        "|",
        "{:02d}".format(board[8]),
    )
    print("------------")