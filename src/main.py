import time
from boardUtils import *
print("Masukkan nama Test case! : ", end='')
filestr = input()
print("Apakah ingin menampilkan alur solusi? (Y/N)")
ans = input()
verbose = False
if (ans.lower() == "y"):
    verbose = True
f = open("./test/" + filestr)
inp = list(map(int, f.read().split(" ")))

QueuePenelusuran = []
ditelusuri = []

test = 0
start = time.time()
if (reachable(inp) % 2 == 0):
    found = False
    step = []
    append(QueuePenelusuran, inp.copy(), -1, step.copy())
    while QueuePenelusuran and not found:
        test += 1
        cc, cb, prev, steps = QueuePenelusuran.pop(0)
        if (cb in ditelusuri):
            #kalo udah ditelusuri g dicek lagi
            continue
        ditelusuri.append(cb.copy())

        if cc == 0:
            found = True
            end = time.time()
            break
        idx = getindex(cb, 16)
        i = idx // 4
        j = idx % 4
        # up = 0, down = 1, left = 2, right = 3
        if (i != 0 and prev != 1): #biar ga balik lagi
            goUp(cb)
            if (cb not in ditelusuri):
                append(QueuePenelusuran, cb.copy(), 0, steps.copy())
            goDown(cb)
        if (i != 3 and prev != 0):
            goDown(cb)
            if (cb not in ditelusuri):
                append(QueuePenelusuran, cb.copy(), 1, steps.copy())
            goUp(cb)
        if (j != 0 and prev != 3):
            goLeft(cb)
            if (cb not in ditelusuri):
                append(QueuePenelusuran, cb.copy(), 2, steps.copy())
            goRight(cb)
        if (j != 3 and prev != 2):
            goRight(cb)
            if (cb not in ditelusuri):
                append(QueuePenelusuran, cb.copy(), 3, steps.copy())
            goLeft(cb)
    if found:
        if verbose:
            printStep(inp, steps)
        print("Menulusuri total " + str(len(ditelusuri)) + " kemungkinan." )
        print("Panjang Jalur solusi adalah " + str(len(steps)) + " Simpul")
        print("waktu algoritma ", end='')
        print(end-start, end=' detik\n')

