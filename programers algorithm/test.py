# solution
a = [9,-1,-5]
result = 3
a1 = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
result1 = 6

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

print(solution(a1))