'''
숫자야구

숫자 야구 게임이란 2명이 서로가 생각한 숫자를 맞추는 게임입니다.
각자 서로 다른 1~9까지 3자리 임의의 숫자를 정한 뒤 서로에게 3자리의 숫자를 불러서 결과를 확인합니다. 그리고 그 결과를 토대로 상대가 정한 숫자를 예상한 뒤 맞힙니다.

* 숫자는 맞지만, 위치가 틀렸을 때는 볼
* 숫자와 위치가 모두 맞을 때는 스트라이크
* 숫자와 위치가 모두 틀렸을 때는 아웃

질문한 세 자리의 수, 스트라이크의 수, 볼의 수를 담은 2차원 배열 baseball이 매개변수로 주어질 때, 가능한 답의 개수를 return 하도록 solution 함수를 작성해주세요.


제한사항

질문의 수는 1 이상 100 이하의 자연수입니다.
baseball의 각 행은 [세 자리의 수, 스트라이크의 수, 볼의 수] 를 담고 있습니다.


# input
baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

# return
2

'''

# solution

baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

import itertools

def solution(baseball):
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = 0
    want = len(baseball)
    for i in range(len(baseball)):
        baseball[i][0] = str(baseball[i][0])
    stack = list(itertools.permutations(num, 3))
    for i in stack:
        cnt = 0
        for j in baseball:
            strike = 0
            ball = 0
            for k in range(3):
                if i[k] == j[0][k]:
                    strike += 1
            for k in range(3):
                if j[0][k] in i:
                    ball += 1
            ball = ball - strike
            if strike == j[1]:
                if ball == j[2]:
                    cnt += 1
        if cnt == want:
            result += 1
    return result

print(solution(baseball))
