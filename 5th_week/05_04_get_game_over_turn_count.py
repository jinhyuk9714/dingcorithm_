# 말의 개수
k = 4

# 체스판 상태 (0: 흰색, 1: 빨간색, 2: 파란색)
chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# 말들의 초기 위치 및 방향 설정 (행, 열, 방향)
start_horse_location_and_directions = [
    [0, 0, 0],  # 0번 말: (0,0) → 방향
    [0, 1, 0],  # 1번 말: (0,1) → 방향
    [0, 2, 0],  # 2번 말: (0,2) → 방향
    [2, 2, 2]   # 3번 말: (2,2) ↑ 방향
]

# 방향 벡터 (0: →, 1: ←, 2: ↑, 3: ↓)
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    turn_count = 1

    # 체스판 위 말들의 스택 상태를 기록할 2차원 리스트
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]

    # 초기 말의 위치를 맵에 반영
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)

    # 최대 1000턴까지 반복
    while turn_count <= 1000:
        for horse_index in range(horse_count):
            r, c, d = horse_location_and_directions[horse_index]
            new_r, new_c = r + dr[d], c + dc[d]

            # 이동하려는 위치가 범위를 벗어나거나 파란색이면 방향을 반대로 바꿈
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = reverse_direction(d)
                new_r, new_c = r + dr[new_d], c + dc[new_d]
                horse_location_and_directions[horse_index][2] = new_d

                # 반대 방향도 막혀 있으면 이동하지 않음
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            # 해당 말부터 위에 쌓인 말들만 분리
            for i, current_horse_index in enumerate(current_stacked_horse_map[r][c]):
                if current_horse_index == horse_index:
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break

            # 빨간 칸이라면 말들의 순서를 뒤집음
            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)

            # 이동한 위치로 말 이동
            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                horse_location_and_directions[moving_horse_index][0] = new_r
                horse_location_and_directions[moving_horse_index][1] = new_c

            # 말이 4개 이상 쌓이면 게임 종료
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count

        turn_count += 1

    # 1000턴을 넘어도 게임이 종료되지 않으면 -1 반환
    return -1

# 방향을 반대로 바꾸는 함수
def reverse_direction(d):
    return d + 1 if d % 2 == 0 else d - 1

# 테스트 케이스 실행
print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환되어야 함

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 푸리 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 푸리 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))
