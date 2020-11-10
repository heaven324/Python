# solution

n = 4
# result = [1,2,9,3,10,8,4,5,6,7]
n = 5
# result = [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
n = 6
# result = [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]

from itertools import chain

def solution(n):
    maps = [[0 for _ in range(n)] for _ in range(n)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            maps[x][y] = num
            num += 1
    answer = [i for i in chain(*maps) if i != 0]
    return answer


print(solution(n))


'''
삼각 달팽이
문제 설명
정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 
맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 
모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

examples.png

제한사항
n은 1 이상 1,000 이하입니다.
입출력 예
n   result
4   [1,2,9,3,10,8,4,5,6,7]
5   [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
6   [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.
입출력 예 #2

문제 예시와 같습니다.
입출력 예 #3

문제 예시와 같습니다.
'''