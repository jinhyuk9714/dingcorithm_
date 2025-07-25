top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders_stack(heights):
    answer = [0] * len(heights)

    while heights:
        height = heights.pop()
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > height:
                answer[len(heights)] = i + 1
                break
    return answer


print(get_receiver_top_orders_stack(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ", get_receiver_top_orders_stack([6, 9, 5, 7, 4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ", get_receiver_top_orders_stack([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ", get_receiver_top_orders_stack([1, 5, 3, 6, 7, 6, 5]))
