# solution
a = [9,-1,-5]
result = 3
a1 = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
result1 = 6


def solution(a):
    lef_min = 0
    rig_min = len(a) - 1
    if len(a) <= 2:
        return len(a)
    answer = 2
    while rig_min - lef_min != 1:
        lrmax = max(a[lef_min], a[rig_min])
        if lrmax == a[lef_min]:
            if a[lef_min] < a[lef_min+1]:
                switch = 0
                tmp = 1
                while switch != 1:
                    tmp += 1
                    if a[lef_min] < a[lef_min + tmp]:
                        continue
                    elif a[lef_min] > a[lef_min + tmp] and a[lef_min + tmp] != a[rig_min]:
                        lef_min += tmp
                        switch = 1
                        answer += 1
                    elif a[lef_min + tmp] == a[rig_min]:
                        return answer
            else: 
                lef_min += 1
                answer += 1
        else:
            if a[rig_min] < a[rig_min-1]:
                switch = 0
                tmp = 1
                while switch != 1:
                    tmp += 1
                    if a[rig_min] < a[rig_min - tmp]:
                        continue
                    elif a[rig_min] > a[rig_min - tmp] and a[rig_min - tmp] != a[lef_min]:
                        rig_min -= tmp
                        switch = 1
                        answer += 1
                    elif a[rig_min - tmp] == a[lef_min]:
                        return answer
            else:
                rig_min -= 1
                answer += 1
    return answer

print(solution(a1))

'''
시간 복잡도 때문에 효율성이 안나온 나의 첫 풀이
    혹시 나중에 보게된다면 이 아이디어로 해결할 수 있는 방법이 있는지 생각해봅시다

def solution(a):
    answer = 1
    min_ind = a.index(min(a))
    lef = a[:min_ind]
    rig = a[min_ind+1:]
    rig_min = -1
    while rig[rig_min+1:] != []:
        rig_min = rig.index(min(rig[rig_min+1:]))
        answer += 1
    lef_min = len(lef)
    while lef[:lef_min] != []:
        lef_min = lef.index(min(lef[:lef_min]))
        answer += 1
    return answer


문제 설명
일렬로 나열된 n개의 풍선이 있습니다. 모든 풍선에는 서로 다른 숫자가 써져 있습니다. 당신은 다음 과정을 반복하면서 풍선들을 단 1개만 남을 때까지 계속 터트리려고 합니다.

임의의 인접한 두 풍선을 고른 뒤, 두 풍선 중 하나를 터트립니다.
터진 풍선으로 인해 풍선들 사이에 빈 공간이 생겼다면, 빈 공간이 없도록 풍선들을 중앙으로 밀착시킵니다.
여기서 조건이 있습니다. 인접한 두 풍선 중에서 번호가 더 작은 풍선을 터트리는 행위는 최대 1번만 할 수 있습니다. 즉, 어떤 시점에서 인접한 두 풍선 중 번호가 더 작은 풍선을 터트렸다면, 그 이후에는 인접한 두 풍선을 고른 뒤 번호가 더 큰 풍선만을 터트릴 수 있습니다.

당신은 어떤 풍선이 최후까지 남을 수 있는지 알아보고 싶습니다. 위에 서술된 조건대로 풍선을 터트리다 보면, 어떤 풍선은 최후까지 남을 수도 있지만, 어떤 풍선은 무슨 수를 쓰더라도 마지막까지 남기는 것이 불가능할 수도 있습니다.

일렬로 나열된 풍선들의 번호가 담긴 배열 a가 주어집니다. 위에 서술된 규칙대로 풍선들을 1개만 남을 때까지 터트렸을 때 최후까지 남기는 것이 가능한 풍선들의 개수를 return 하도록 solution 함수를 완성해주세요.

제한 사항
a의 길이는 1 이상 1,000,000 이하입니다.
a[i]는 i+1 번째 풍선에 써진 숫자를 의미합니다.
a의 모든 수는 -1,000,000,000 이상 1,000,000,000 이하인 정수입니다.
a의 모든 수는 서로 다릅니다.
입출력 예
a	result
[9,-1,-5]	3
[-16,27,65,-2,58,-92,-71,-68,-61,-33]	6
입출력 예 설명
입출력 예 #1

첫 번째 풍선(9가 써진 풍선)을 최후까지 남기는 방법은 다음과 같습니다.
[9, -1, -5] 에서 -1, -5가 써진 풍선을 고른 뒤, -1이 써진 풍선(번호가 더 큰 것)을 터트립니다.
[9, -5] 에서 9, -5가 써진 풍선을 고른 뒤, -5가 써진 풍선(번호가 더 작은 것)을 터트립니다.
두 번째 풍선(-1이 써진 풍선)을 최후까지 남기는 방법은 다음과 같습니다.
[9, -1, -5] 에서 9, -1이 써진 풍선을 고른 뒤, 9가 써진 풍선(번호가 더 큰 것)을 터트립니다.
[-1, -5] 에서 -1, -5가 써진 풍선을 고른 뒤, -5가 써진 풍선(번호가 더 작은 것)을 터트립니다.
세 번째 풍선(-5가 써진 풍선)을 최후까지 남기는 방법은 다음과 같습니다.
[9, -1, -5] 에서 9, -1이 써진 풍선을 고른 뒤, 9가 써진 풍선(번호가 더 큰 것)을 터트립니다.
[-1, -5] 에서 -1, -5가 써진 풍선을 고른 뒤, -1이 써진 풍선(번호가 더 큰 것)을 터트립니다.
3개의 풍선이 최후까지 남을 수 있으므로, 3을 return 해야 합니다.
입출력 예 #2

최후까지 남을 수 있는 풍선은 -16, -92, -71, -68, -61, -33이 써진 풍선으로 모두 6개입니다.
'''
