# 주어진 시간(time) 기준으로 1초(1000ms) 동안 처리 중인 요청 개수를 세는 함수
def get_request_count_during_one_second(time, start_and_end_times):
    request_count = 0
    start = time  # 1초 구간 시작 시간
    end = time + 1000  # 1초 구간 끝 시간 (1초 = 1000ms)

    for start_time, end_time in start_and_end_times:
        # 처리 구간이 1초 구간과 겹치면 count (닫힌 구간 [start, end))
        # 즉, 요청 종료 시각이 구간 시작보다 크거나 같고,
        # 요청 시작 시각이 구간 끝보다 작으면 겹친다고 판단
        if end_time >= start and start_time < end:
            request_count += 1

    return request_count


def solution(lines):
    answer = 0
    start_and_end_times = []  # 각 요청의 시작 시각, 종료 시각 (밀리초 단위) 저장

    for line in lines:
        # 로그 형식: "2016-09-15 01:00:04.002 2.0s"
        _, time_str, duration_str = line.split()

        # 종료 시각 파싱
        hh, mm, ss = time_str.split(':')
        end_time = (int(hh) * 3600 + int(mm) * 60 + float(ss)) * 1000  # 종료 시각을 ms로 변환

        # 처리 시간 파싱 ("2.0s" → 2000ms)
        duration = float(duration_str.replace('s', '')) * 1000

        # 시작 시각 계산: 요청 시작 시각 = 종료시각 - 처리시간 + 1ms
        # +1ms 이유: 문제에서 처리 시간은 "끝나는 시각 - 시작 시각 + 1초"의 의미이기 때문
        start_time = end_time - duration + 1

        # (시작시간, 종료시간) 튜플 저장
        start_and_end_times.append([start_time, end_time])

    # 모든 요청의 시작 시각과 종료 시각을 기준으로
    # 해당 시각부터 1초 동안의 최대 동시 처리량 계산
    for start_time, end_time in start_and_end_times:
        # 각 요청의 시작 시각, 종료 시각을 기준으로 1초 구간 잡기
        # → 모든 로그 구간을 검사하면 누락이 없음
        answer = max(
            answer,
            get_request_count_during_one_second(start_time, start_and_end_times),
            get_request_count_during_one_second(end_time, start_and_end_times)
        )

    return answer


lines = [
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
]
print(solution(lines))  # 1

lines = [
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]
print(solution(lines))  # 2

lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]
print(solution(lines))  # 7
