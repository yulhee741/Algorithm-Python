# 절댓값 힙
import sys
import heapq # 최소힙

oprtN = int(sys.stdin.readline())

heap = []
result = []
for _ in range(oprtN):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap,[abs(x), x]) # 최소힙에 절댓값 x를 넣음 => 절댓값이 작은 순서로 힙에 저장됨.
        #절댓값이 같은경우, 원래의 수도 고려해야하기 때문에 배열 쌍으로 저장
    else:
        if len(heap) == 0:
            result.append(0)
        else:
            result.append(heapq.heappop(heap)[1])
            

print(heap)
for i in result:
    print(i)



