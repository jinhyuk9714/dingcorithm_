def find_max_plus_or_multiply(array):
    current = array[0]
    for i in range(1, len(array)):
        if current * array[i] < current + array[i]:
            current += array[i]
        else:
            current *= array[i]
        # print(f"현재값: {current}")
    return current

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0, 3, 5, 6, 1, 2, 4]))
print("정답 = 8820 현재 풀이 값 =", result([3, 2, 1, 5, 9, 7, 4]))
print("정답 = 270 현재 풀이 값 =", result([1, 1, 1, 3, 3, 2, 5]))
