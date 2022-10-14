""" R(뒤집기),D(버리기) R 은 배열에 있는 수의 순서를 뒤집음, D는 첫 번째 수를 버리는 함수(비어있는데 쓰면 오류) """


import sys
from collections import deque

T=int(input())

for i in range(T):
    order=sys.stdin.readline().rstrip()
    n=int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    num = deque(arr)
    
    rev, front, back = 0, 0, len(num)-1
    flag = 0
    if n == 0:
        num = []
        front = 0
        back = 0
    
    for j in order:
        if j=='R':
            rev += 1
            
        elif j=='D':
            if len(num)<1:
                print("error")
                flag +=1
                break
            else :
                if rev %2 == 0:
                    num.popleft()
                    
                else:
                    num.pop()
                    #print(num)
    
    if flag ==0:
        if rev%2==0:
            print("["+",".join(num)+"]")
        else :
            num.reverse()
            print("["+",".join(num)+"]")

""" import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")     """