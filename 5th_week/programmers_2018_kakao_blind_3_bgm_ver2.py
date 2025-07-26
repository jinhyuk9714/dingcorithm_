def normalize_melody(melody):
    """
    # 멜로디를 통일된 형식으로 변환
    # C#, D# 등을 소문자로 치환해 'C'와 'C#'을 구분 가능하게 만듦
    """
    return melody.replace('C#', 'c')\
                 .replace('D#', 'd')\
                 .replace('F#', 'f')\
                 .replace('G#', 'g')\
                 .replace('A#', 'a')\
                 .replace('B#', 'b')


def to_minutes(time_str):
    """문자열 시각을 분 단위로 변환"""
    h, m = map(int, time_str.split(":"))
    return h * 60 + m


def solution(m, musicinfos):
    m = normalize_melody(m)
    answer = "(None)"
    max_duration = -1

    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start_min = to_minutes(start)
        end_min = to_minutes(end)

        duration = end_min - start_min
        if duration < 0:  # 자정 넘김 보정
            duration += 24 * 60

        # 멜로디 변환
        melody = normalize_melody(melody)

        # 재생된 멜로디 생성
        full_melody = (melody * (duration // len(melody) + 1))[:duration]

        # 기억한 멜로디가 포함되어 있는지 확인
        if m in full_melody:
            if duration > max_duration:  # 가장 긴 곡 우선
                max_duration = duration
                answer = title

    return answer


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))  # "HELLO"

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))  # "FOO"

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))  # "WORLD"
