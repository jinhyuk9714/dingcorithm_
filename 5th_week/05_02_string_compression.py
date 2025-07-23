input = "abcabcabcabcdededededede"


# 문자열 길이 1,000 이하 -> N^2 까지는 OK -> 브루트포스(완전탐색) 가능
def string_compression(s):
    min_len = len(s)

    for i in range(1, len(s) // 2 + 1):
        compressed = []
        prev = s[0:i]
        count = 1

        for j in range(i, len(s), i):
            cur = s[j:j + i]
            if cur == prev:
                count += 1
            else:
                if count > 1:
                    compressed.append(str(count))
                compressed.append(prev)
                prev = cur
                count = 1

        if count > 1:
            compressed.append(str(count))
        compressed.append(prev)

        compressed_str = ''.join(compressed)
        min_len = min(min_len, len(compressed_str))

    return min_len


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))
