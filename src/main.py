from boardUtils import *
f = open("./test/test2.txt")
inp = list(map(int, f.read().split(" ")))
printBoard(inp)
QueuePenelusuran = []
ditelusuri = []
# swap(inp, 1, 14)
# printBoard(inp)
test = 0
if (reachable(inp) % 2 == 0):
    found = False
    append(QueuePenelusuran, inp.copy(), -1)
    while QueuePenelusuran and not found:
        test += 1
        cc, cb, prev = QueuePenelusuran.pop(0)
        if (cb in ditelusuri):
            continue
        ditelusuri.append(cb.copy())
        # printBoard(cb)
        # print(cc)
        # print(cc)
        if cc == 0:
            found = True
            break
        idx = getindex(cb, 16)
        i = idx // 4
        j = idx % 4
        # up = 0, down = 1, left = 2, right = 3
        if (i != 0 and prev != 1): #biar ga balik lagi
            goUp(cb)
            if (cb not in ditelusuri):
                append(QueuePenelusuran, cb.copy(), 0)
            goDown(cb)
        if (i != 3 and prev != 0):
            goDown(cb)
            if (cb not in ditelusuri):
                append(QueuePenelusuran, cb.copy(), 1)
            goUp(cb)
        if (j != 0 and prev != 3):
            goLeft(cb)
            if (cb not in ditelusuri):
                append(QueuePenelusuran, cb.copy(), 2)
            goRight(cb)
        if (j != 3 and prev != 2):
            goRight(cb)
            if (cb not in ditelusuri):
                append(QueuePenelusuran, cb.copy(), 3)
            goLeft(cb)
    # while(cost(inp) != 0):
    #     printBoard(inp)
    #     listPenelusuran.append(inp.copy())
    #     listcost = []
    #     idx = getindex(inp, 16)
    #     i = idx // 4
    #     j = idx % 4
    #     if (i != 0):
    #         goUp(inp)
    #         if (inp in listPenelusuran):
    #             listcost.append(9999)
    #         else:
    #             listcost.append(cost(inp))
    #         goDown(inp)
    #     else:
    #         listcost.append(9999)
    #     if (i != 3):
    #         goDown(inp)
    #         if (inp in listPenelusuran):
    #             listcost.append(9999)
    #         else:
    #             listcost.append(cost(inp))
    #         goUp(inp)
    #     else:
    #         listcost.append(9999)
    #     if (j != 0):
    #         goLeft(inp)
    #         if (inp in listPenelusuran):
    #             listcost.append(9999)
    #         else:
    #             listcost.append(cost(inp))
    #         goRight(inp)
    #     else:
    #         listcost.append(9999)
    #     if (j != 3):
    #         goRight(inp)
    #         if (inp in listPenelusuran):
    #             listcost.append(9999)
    #         else:
    #             listcost.append(cost(inp))
    #         goLeft(inp)
    #     else:
    #         listcost.append(9999)
    #     imin = listcost.index(min(listcost))
    #     print(listcost)
    #     if (imin == 0):
    #         goUp(inp)
    #     elif (imin == 1):
    #         goDown(inp)
    #     elif (imin == 2):
    #         goLeft(inp)
    #     else:
    #         goRight(inp)
    #     pprev = prev
    #     prev = imin


    if found:
        printBoard(cb)
        print("Menulusuri total " + str(len(ditelusuri)) + " kemungkinan." )

