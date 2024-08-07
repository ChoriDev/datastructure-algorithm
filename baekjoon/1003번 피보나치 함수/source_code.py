import math

def get_points_count(x1, y1, r1, x2, y2, r2):
    d = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)) # 중심 거리

    if d == 0 and r1 == r2:
        return -1 # 다른 한 점이 존재할 수 있는 위치 개수, 무한대면 -1
    elif d == 0 and r1 != r2:
        return 0
    elif d < abs(r1 - r2):
        return 0
    elif d > (r1 + r2):
        return 0
    elif d == (r1 + r2):
        return 1
    elif d == abs(r1 - r2):
        return 1
    else:
        return 2

T = int(input()) # 테스트 케이스의 수

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    count = get_points_count(x1, y1, r1, x2, y2, r2)

    print(count)