# 멜로디 문자열을 '# 음' 포함한 단일 음 리스트로 변환
def split_melody(melody_str):
    result = []
    i = 0
    while i < len(melody_str):
        if i + 1 < len(melody_str) and melody_str[i + 1] == '#':
            result.append(melody_str[i] + '#')  # 예: 'C#'
            i += 2
        else:
            result.append(melody_str[i])  # 예: 'C'
            i += 1
    return result


# HH:MM 형식을 분(minute) 단위 정수로 변환
def to_minutes(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m


# 재생 시간 계산 (자정을 넘긴 경우도 포함)
def get_play_time(start, end):
    start_min = to_minutes(start)
    end_min = to_minutes(end)
    if end_min < start_min:  # 23:00 ~ 00:10 같은 경우 처리
        end_min += 24 * 60
    return end_min - start_min


# 메인 함수
def solution(m, musicinfos):
    answer = None
    max_duration = -1  # 가장 긴 재생 시간을 가진 곡만 채택
    m_arr = split_melody(m)  # 기억한 멜로디 분해

    for info in musicinfos:
        start_time, end_time, title, melody = info.split(',')
        duration = get_play_time(start_time, end_time)
        melody_arr = split_melody(melody)

        # 실제 재생된 멜로디 생성 (재생 시간만큼 반복하여 자름)
        played_melody = (melody_arr * ((duration // len(melody_arr)) + 1))[:duration]

        # 부분 문자열 비교: 기억한 멜로디가 재생 멜로디에 포함되는지 확인
        for i in range(len(played_melody) - len(m_arr) + 1):
            if played_melody[i:i + len(m_arr)] == m_arr:
                if duration > max_duration:
                    max_duration = duration
                    answer = title
                break  # 하나라도 매칭되면 종료

    return answer if answer else "(None)"


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))  # "HELLO"

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))  # "FOO"

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))  # "WORLD"
