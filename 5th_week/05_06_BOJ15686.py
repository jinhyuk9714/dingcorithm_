import itertools, sys

# 도시의 크기 N, 선택할 치킨집 수 M
n, m = map(int, input().split())

# 도시 정보: 0 = 빈 칸, 1 = 집, 2 = 치킨집
city_map = [list(map(int, input().split())) for _ in range(n)]


def get_min_city_chicken_distance(n, m, city_map):
    house_locations = []  # 집들의 위치 저장
    chicken_locations = []  # 치킨집들의 위치 저장
    min_total = sys.maxsize  # 도시의 최소 치킨 거리 (최솟값으로 갱신할 예정)

    # 1. 집과 치킨집 위치 수집
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                house_locations.append((i, j))
            elif city_map[i][j] == 2:
                chicken_locations.append((i, j))

    # 2. 치킨집 중 M개를 선택하는 모든 조합 생성
    chicken_combinations = itertools.combinations(chicken_locations, m)

    # 3. 각 조합마다 도시의 치킨 거리 계산
    for comb in chicken_combinations:
        total_distance = 0

        # 각 집마다 → 가장 가까운 치킨집과의 거리 계산
        for hx, hy in house_locations:
            min_dist = sys.maxsize
            for cx, cy in comb:
                dist = abs(hx - cx) + abs(hy - cy)  # 맨해튼 거리
                min_dist = min(min_dist, dist)
            total_distance += min_dist  # 해당 조합에 대한 도시 치킨 거리 누적

        # 도시의 치킨 거리 최소값 갱신
        min_total = min(min_total, total_distance)

    return min_total


# 테스트 케이스 실행
print(get_min_city_chicken_distance(n, m, city_map))  # 5

city_map = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0]
]
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5, 1, city_map))

city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5, 2, city_map))
