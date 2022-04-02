def cost(list):
    count = 0
    for i in range(15):
        if list[i]!=i+1:
            count+=1
    return count
def getindex(list, x):
    for i in range(len(list)):
        # print(i,x)
        if list[i] == x:
            return i
        
def kurang(list,i):
    count = 0
    for j in range(getindex(list, i), 16):
        if (list[j] < i):
            count+=1
    return count
def X(list):
    arsir = [1,3, 4,6, 9, 11, 12,14]
    idx = getindex(list, 16)
    if (idx in arsir):
        return 1
    else:
        return 0
def reachable(list):
    sum = 0
    for i in range(1,17):
        sum += kurang(list, i)
    sum += X(list)
    return sum
def goUp(list):
    idx = getindex(list,16)
    i = idx // 4
    j = idx % 4
    if (i != 0):
        swap(list, (i - 1) * 4 + j, idx)
def goDown(list):
    idx = getindex(list,16)
    i = idx // 4
    j = idx % 4
    if (i != 3):
        swap(list, (i + 1) * 4 + j, idx)
def goLeft(list):
    idx = getindex(list,16)
    i = idx // 4
    j = idx % 4
    if (j != 0):
        swap(list, i * 4 + j-1, idx)
def goRight(list):
    idx = getindex(list, 16)
    i = idx // 4
    j = idx % 4
    if (j != 3):
        swap(list, i * 4 + j+1, idx)
def swap(list, i ,j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
def printBoard(list):
    for i in range(4):
        for j in range(4):
            print(str(list[i*4 + j]).rjust(3," "), end=' ')
        print()
def append(q, board, prev, step):
    c = cost(board)
    step.append(prev)
    q.append((c, board, prev, step))
    q.sort()
def isGoal(board):
    for i in range(16):
        if board[i]!=i+1:
            return False
    return True
def printStep(board, step):
    for i in range(len(step)):
        if (step[i] == 0):
            goUp(board)
            print("UP")
        if (step[i] == 1):
            goDown(board)
            print("DOWN")
        if (step[i] == 2):
            goLeft(board)
            print("LEFT")
        if (step[i] == 3):
            goRight(board)
            print("RIGHT")
        printBoard(board)