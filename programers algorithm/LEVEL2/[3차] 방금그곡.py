# solution

m = "ABCDEFG"
musicinfos = ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']

# m = "CC#BCC#BCC#BCC#B"
# musicinfos = ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']

# m = 'ABC'
# musicinfos = ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']	

    
def incoding_m(m):
    m = m.replace("C#", "c")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")
    m = m.replace("A#", "a")
    return m


def time_cal(t1, t2):
    ti1 = int(t1[0:2])*60 + int(t1[3:])
    ti2 = int(t2[0:2])*60 + int(t2[3:])
    return ti2 - ti1

def solution(m, musicinfos):
    m = incoding_m(m)
    answer = ""
    answer_time = 0
    for obj in musicinfos:
        obj = obj.split(",")
        time = time_cal(obj[0], obj[1])
        music = incoding_m(obj[3])
        len_m = len(music)
        music = music*(time // len_m) + music[:(time % len_m)]
        if m in music and answer_time < time:
            answer = obj[2]
            answer_time = time
    return "(None)" if len(answer) == 0 else answer





print(solution(m, musicinfos))

