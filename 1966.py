test_num = int(input())


queue=[]

for i in range(test_num):
    n , m = list(map(int,input().split()))
    sig = list(map(int,input().split()))
    idx = list(range(len(sig)))
    idx[m]="target"

    order = 0

    while True : 
        if sig[0]==max(sig):
            order +=1

            if idx[0]=="target":
                print(order)
                break
            else : 
                sig.pop(0)
                idx.pop(0)
        else : 
            sig.append(sig.pop(0))
            idx.append(idx.pop(0))