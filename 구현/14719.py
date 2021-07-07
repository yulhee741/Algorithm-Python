#빗물
from sys import stdin

H, W = map(int, stdin.readline().split())
buildings = list(map(int, stdin.readline().split()))

def solution(buildings):
    rain = 0
    for i in range(len(buildings)):
        # 현재 인덱스의 왼쪽에서 가장 높은 건물의 높이        
        max_left = max(buildings[:i+1])
        # 현재 인덱스의 오른쪽에서 가장 높은 건물의 높이 
        max_right = max(buildings[i:])
        # 둘중에 어떤 값이 더 작은지 확인
        which_low = min(max_left, max_right)
        rain = rain + abs(buildings[i] - which_low)
    return rain

print(solution(buildings))