# solution

number, k = "1231234", 3

def solution(number, k):
    cnt = 0
    ind = 0
    while cnt < k:
        ind_switch = 1
        if ind == len(number) - 1:
            number = number[:ind]
            cnt += 1
            ind = ind -2
        if int(number[ind]) < int(number[ind+1]):
            number = number[:ind] + number[ind+1:]
            if ind != 0:
                ind_switch = -1
            else:
                ind_switch = 0
            cnt += 1
        ind += ind_switch
    return number

print(solution(number, k))

"""
나의 풀이

number의 숫자 하나하나 지나가면서 다음 숫자와 크기 비교를 통해 지금 숫자가 더 작을 때 제거 하는 방법
마지막 인덱스까지 오면 자연스럽게 마지막 인덱스를 제거
for 문 보다는 while문이 인덱스를 원하는대로 조작할 수 있어서 while문을 사용
"""

'''

문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 
이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. 
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 
solution 함수를 완성하세요.


제한 조건

number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.

입출력 예

number        k   return
"1924"        2   "94"
"1231234"     3   "3234"
"4177252841"  4   "775841"

'''
