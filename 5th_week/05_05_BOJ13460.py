from collections import deque

n, m = map(int, input().split())  # N x M 입력

# 예시 맵 (테스트용)
game_map = [list(input()) for _ in range(n)]


# 방향: 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 벽(#)이나 구멍(O)을 만날 때까지 공을 굴리는 함수
def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0
    # 다음 칸이 벽이 아니고, 현재 위치가 구멍이 아니라면 계속 이동
    while game_map[r + diff_r][c + diff_c] != '#' and game_map[r][c] != 'O':
        r += diff_r
        c += diff_c
        move_count += 1
    return r, c, move_count


# 빨간 구슬만 구멍으로 빼낼 수 있는지 확인하는 함수 (10회 이하 시도)
def is_available_to_take_out_only_red_marble(n, m, game_map):
    # visited[red_r][red_c][blue_r][blue_c] = True → 방문 여부 체크
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue = deque()

    # 빨간 구슬(R), 파란 구슬(B) 위치 초기화
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == 'R':
                red_row, red_col = i, j
            if game_map[i][j] == 'B':
                blue_row, blue_col = i, j

    # BFS 시작: (빨간구슬 좌표, 파란구슬 좌표, 시도횟수)
    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()

        # 10번 초과하면 실패 처리
        if try_count >= 11:
            break

        # 4방향으로 기울이기 시도
        for i in range(4):
            # 빨간 구슬 이동
            next_red_row, next_red_col, red_move_count = move_until_wall_or_hole(
                red_row, red_col, dr[i], dc[i], game_map
            )
            # 파란 구슬 이동
            next_blue_row, next_blue_col, blue_move_count = move_until_wall_or_hole(
                blue_row, blue_col, dr[i], dc[i], game_map
            )

            # 파란 구슬이 구멍에 빠졌으면 실패 → 다음 시도
            if game_map[next_blue_row][next_blue_col] == 'O':
                continue

            # 빨간 구슬만 구멍에 빠졌으면 성공
            if game_map[next_red_row][next_red_col] == 'O':
                return try_count

            # 두 구슬이 같은 위치에 도착했다면 → 이동 거리 비교해서 하나를 뒤로 물림
            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if red_move_count > blue_move_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]

            # 방문하지 않은 상태라면 큐에 추가
            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((
                    next_red_row, next_red_col,
                    next_blue_row, next_blue_col,
                    try_count + 1
                ))

    # 빨간 구슬만 탈출할 수 없으면 -1
    return -1


# 테스트: 빨간 구슬만 구멍에 빠질 수 있는지 확인
print(is_available_to_take_out_only_red_marble(n, m, game_map))
