import re
from itertools import permutations

def solution(expression):
    # 1. 숫자와 연산자를 분리
    # re.findall로 숫자만 추출 → '100-200*300' → ['100', '200', '300']
    numbers = list(map(int, re.findall(r'\d+', expression)))  # 정수형으로 변환
    # re.findall로 연산자만 추출 → ['-', '*', '-']
    operators = re.findall(r'[\*\+\-]', expression)

    # 2. 가능한 연산자 우선순위 모든 순열 생성 (예: ('-', '*', '+'))
    operator_permutations = list(permutations(['*', '+', '-']))

    max_result = 0  # 결과 중 가장 큰 절댓값 저장

    # 3. 각 우선순위 조합에 대해 시뮬레이션 수행
    for operator_order in operator_permutations:
        # 리스트 복사 (원본이 바뀌지 않도록)
        temp_numbers = numbers[:]
        temp_operators = operators[:]

        # 현재 우선순위에 따라 연산 처리
        for op in operator_order:
            index = 0
            while index < len(temp_operators):
                if temp_operators[index] == op:
                    # 현재 연산자가 일치하면 계산 수행
                    if op == '*':
                        result = temp_numbers[index] * temp_numbers[index + 1]
                    elif op == '+':
                        result = temp_numbers[index] + temp_numbers[index + 1]
                    else:  # '-'
                        result = temp_numbers[index] - temp_numbers[index + 1]

                    # 계산 결과 반영
                    temp_numbers[index] = result          # index 위치에 결과 대입
                    temp_numbers.pop(index + 1)           # 사용한 다음 숫자 제거
                    temp_operators.pop(index)             # 해당 연산자 제거
                    # index는 유지 (현재 위치에 새 연산자가 올 수 있으므로)
                else:
                    index += 1  # 현재 연산자와 다르면 다음 위치로 이동

        # 모든 연산 후 temp_numbers[0]이 결과
        max_result = max(max_result, abs(temp_numbers[0]))  # 절댓값 비교

    return max_result  # 최대 절댓값 반환



expression = "100-200*300-500+20"
# 60420 이 출력되어야 합니다.

print(solution(expression))
