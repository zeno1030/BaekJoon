import sys
import heapq

input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
inf=sys.maxsize

for i in range(E):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
v1,v2=map(int,input().split())

def Dijkstra(start):
    #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    dp = [inf for i in range(N + 1)]
    dp[start] = 0
    heap = []
    heapq.heappush(heap,(0, start))

    #힙에 원소가 없을 때 까지 반복.
    while heap:
        wei, now = heapq.heappop(heap)        

        for next_wei, next_node in graph[now]:
            #현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
            # = 다음 노드까지의 가중치(next_wei)
            w = next_wei + wei
            #다음 노드까지의 가중치(next_wei)가 현재 기록된 값 보다 작으면 조건 성립.
            if w< dp[next_node]:
                #계산했던 next_wei를 가중치 테이블에 업데이트.
                dp[next_node] = w
                #다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
                heapq.heappush(heap,(next_wei,next_node))
        return dp

#초기화
one = Dijkstra(1)
v1_ = Dijkstra(v1)
v2_ = Dijkstra(v2)
cnt = min(one[v1] + v1_[v2] + v2_[N], one[v2] + v2_[v1] + v1_[N])
print(cnt if cnt < inf else -1)
