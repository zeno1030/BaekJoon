import sys

size = int(sys.stdin.readline()) 
queue = []

for i in range(size) : 
    order = sys.stdin.readline().split()

    if order[0]=="add":
        queue.insert(0,order[1])
    if order[0]=="remove":
        if len(queue) !=0: print(queue.pop())
        else : print(-1)
    if order[0]=="check":
        if len(queue) !=0 : print(0)
        else : print(1)
    if order[0]=="toggle":
        print(len(queue))
    if order[0]=="all":
        if len(queue) != 0 : print(queue[0])
        else : print(-1)
    if order[0]=="empty":
        if len(queue)!=0 : print(queue[len(queue)-1])
        else : print(-1)