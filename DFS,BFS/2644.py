# 촌수계산
from sys import stdin
from collections import deque

# 전체 사람의 수
n = int(stdin.readline().rstrip())
# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
a, b = map(int, stdin.readline().split())
# 부모 자식들 간의 관계의 개수
m = int(stdin.readline().rstrip())

link = [[0] for _ in range(n+1)]
visited = [0] * (n+1)

# x, y 입력 받기
for _ in range(m):
    x, y = map (int, stdin.readline().split())
    link[x].append(y)
    link[y].append(x)

def bfs(num):
    dQ = deque()
    dQ.append(num)
    visited[num]  = 1
    result = 0
    while dQ:
        result += 1
        for i in range(len(dQ)):
            ch = dQ.popleft()
            # 찾고자하는 b면 함수 종료
            if ch == b:
                return result-1
            # link에서 ch번째 원소 배열 확인하며 0일 경우 1로 바꾸고 0일 경우 덱에 append
            # 부모 노드 1로 가서 자식 2, 3 노드를 확인하게 됨
            for j in link[ch]:
                if visited[j] == 0:
                    visited[j] = 1
                    dQ.append(j)
    return -1

print(bfs(a))