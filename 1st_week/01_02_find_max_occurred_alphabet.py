def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if char.isalpha():
            alphabet_occurrence_array[ord(char) - 97] += 1
    return chr(find_max_num(alphabet_occurrence_array) + 97)


def find_max_num(array):
    max_value = array[0]
    max_array = 0
    for i in range(len(array)):
        if array[i] > max_value: # 가장 앞에 있는 알파벳 출력, 가장 뒤에 있는건 >=
            max_value = array[i]
            max_array = i
    return max_array


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
print(result("bbbccc"))
