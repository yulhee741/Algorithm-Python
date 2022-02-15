# 이진트리 순회(깊이우선탐색)
from sys import stdin

# 전위순회
def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=" ")
        DFS(v*2) # 왼쪽노드
        DFS(v*2+1) # 오른쪽노드

# # 중위순회
def DFS(v):
    if v > 7:
        return
    else:
        DFS(v*2) # 왼쪽노드
        print(v, end=" ")
        DFS(v*2+1) # 오른쪽노드

# 후위순회
def DFS(v):
    if v > 7:
        return
    else:
        DFS(v*2) # 왼쪽노드
        DFS(v*2+1) # 오른쪽노드
        print(v, end=" ")

if __name__=="__main__":
    DFS(1)
