import sys

N , M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
pSum =[[0]*1025 for _ in range(1025)]

for i in range(N):
    for j in range(N):
        pSum[i+1][j+1]=pSum[i+1][j]+pSum[i][j+1]-pSum[i][j] + A[i][j]

for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    result = pSum[x2][y2]-pSum[x1-1][y2]-pSum[x2][y1-1]+pSum[x1-1][y1-1]
    print(result)
