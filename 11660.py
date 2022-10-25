import sys
input = sys.stdin.readline


N , M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
pSum =[[0]*1025 for _ in range(1025)]
# 입력 받으면서 prefix sum을 채움(행,열 1칸씩 더 필요함에 유의)
for i in range(N+1):
    for j in range(N+1):
        pSum[i][j]=pSum[i][j-1]+pSum[i-1][j]-pSum[i-1][j-1] + A[i-1][j-1]

#각 쿼리를 처리
for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    result = pSum[x2][y2]-pSum[x1-1][y2]-pSum[x2][y1-1]+pSum[x1-1][y1-1]
    print(result)
