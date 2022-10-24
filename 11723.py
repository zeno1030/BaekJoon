import sys

size = int(sys.stdin.readline()) 
S=set()

for _ in range(size):
    order = sys.stdin.readline().strip().split()

    if len(order)==1:
        if order[0]=="all":
            S=set([i for i in range(1,21)])
        else : 
            S=set()
    else:
        func, x = order[0], order[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)