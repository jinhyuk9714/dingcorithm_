from itertools import combinations  # 조합을 생성하기 위한 모듈


def make_all_cases(temp):
    """
    예: ["java", "backend", "junior", "pizza"] →
    ['javabackendjuniorpizza', 'javabackendjunior-', ..., '----'] 등 총 16가지 조합 생성
    '-'는 조건을 생략하겠다는 의미 (쿼리에서의 '-'와 매칭)
    """
    cases = []
    for i in range(5):  # 0~4개의 조건을 '-'로 치환
        for combination in combinations([0, 1, 2, 3], i):  # 4개의 조건 중 i개 선택
            case = ''
            for idx in range(4):
                if idx not in combination:
                    case += temp[idx]  # 조건 그대로 사용
                else:
                    case += '-'  # 해당 조건을 '-'로 치환
            cases.append(case)
    return cases


def get_lower_bound(target, array):
    """
    target 이상인 값이 처음 등장하는 위치를 반환
    예: array = [50, 80, 150, 210], target = 150 → 반환값: 2
    """
    current_min = 0
    current_max = len(array)

    while current_min < current_max:
        current_guess = (current_min + current_max) // 2
        if array[current_guess] >= target:
            current_max = current_guess  # 왼쪽도 볼 수 있음
        else:
            current_min = current_guess + 1

    return current_max


def solution(info, query):
    answer = []
    all_cases_from_users = {}  # key: 조건조합(str), value: 해당 조건을 만족하는 지원자들의 점수 리스트

    # 1. info 전처리
    for user_info in info:
        user_info_array = user_info.split()  # ['java', 'backend', 'junior', 'pizza', '150']
        all_cases_from_user = make_all_cases(user_info_array)  # 조건 와일드카드 포함 16가지 조합

        for case in all_cases_from_user:
            if case not in all_cases_from_users:
                all_cases_from_users[case] = [int(user_info_array[4])]  # 점수 저장
            else:
                all_cases_from_users[case].append(int(user_info_array[4]))

    # 2. 점수 정렬 (이진 탐색용)
    for key in all_cases_from_users:
        all_cases_from_users[key].sort()

    for query_info in query:
        query_info_array = query_info.split()  # "java and backend and junior and pizza 100"
        # 필요한 조건들만 추출해 조합 → 조건 키 생성
        case = query_info_array[0] + query_info_array[2] + query_info_array[4] + query_info_array[6]
        score_threshold = int(query_info_array[7])  # 점수 기준값 (이상)

        # 해당 조건 조합이 존재하면
        if case in all_cases_from_users:
            target_users = all_cases_from_users[case]  # 점수 리스트
            count = len(target_users) - get_lower_bound(score_threshold, target_users)
            answer.append(count)
        else:
            answer.append(0)  # 해당 조건 조합 자체가 없음

    return answer


info_array = ["java backend junior pizza 150", "python frontend senior chicken 210",
              "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80",
              "python backend senior chicken 50"]
query_array = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
               "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
               "- and - and - and chicken 100", "- and - and - and - 150"]

print(solution(info_array, query_array))  # [1,1,1,1,2,4] 가 출력되어야 합니다.
