from collections import deque

# 모든 경우의 수 찾기 -> DFS, BFS 사용!!
# 코니의 경우 : 위치가 규칙을 가지고 변함. -> 배열 사용
# 브라운의 경우 : 위치가 랜덤으로 변함. -> 딕셔너리 사용 (임의의 키값 추가 용이)

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 브라운 위치 b, 시간 0 저장

    visited = [{} for _ in range(200001)]  # 브라운의 각 위치마다 시간별 도달 여부 저장

    # 1. 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
    # 2. 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다
    while cony_loc <= 200000:
        cony_loc += time  # 코니의 시간별 위치 저장

        # 현재 시간에 브라운이 cony_loc에 도달 했다면 리턴 (끝)
        if cony_loc <= 200000 and visited[cony_loc].get(time, False):
            return time

        for i in range(0, len(queue)):
            cur_pos, cur_time = queue.popleft()  # brown_loc, 0
            new_time = cur_time + 1

            # 브라운이 1초 후 이동 가능한 위치들 (-1, +1, *2) 탐색
            for new_pos in (cur_pos - 1, cur_pos + 1, cur_pos * 2):
                # 이미 도달한 위치 (True)면 넣지 않음.
                if 0 <= new_pos <= 200000 and not visited[new_pos].get(new_time, False):
                    visited[new_pos][new_time] = True  # 방문 표시
                    queue.append((new_pos, new_time))

        time += 1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10, 3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51, 50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550, 500))
