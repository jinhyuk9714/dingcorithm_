board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1]
]

moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    stack = []
    result = 0

    for move in moves:
        column = move - 1  # 인덱스 보정
        for row in range(len(board)):
            if board[row][column] != 0:
                picked = board[row][column]
                board[row][column] = 0

                if stack and stack[-1] == picked:
                    stack.pop()
                    result += 2
                else:
                    stack.append(picked)

                break  # 인형을 뽑았으면 해당 열에서 더 이상 탐색할 필요 없음

    return result


print(solution(board, moves))
