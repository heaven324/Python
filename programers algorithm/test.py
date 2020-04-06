from itertools import combinations


relation = [["100","ryan","music","2"],   ["200","apeach","math","2"], \
            ["300","tube","computer","3"],["400","con","computer","4"], \
            ["500","muzi","music","3"],   ["600","apeach","music","2"]]







def solution(relation):
    answer = 0
    # 모든 컬럼의 조합 리스트
    all = list()
    #유일성 만족하는 조합 리스트
    uniqeIndex = []
    if len(relation) > 0:
        # 컬럼의 개수
        colSize = len(relation[0])
        # 로우의 개수
        rowSize = len(relation)
        # 모든 컬럼의 조합 구하기 (Set형태)
        for i in range(1, colSize + 1):
            # append는 런타임에러가 뜸 append와 extend 비교하여 알아둘 것
            all.extend([set(k) for k in combinations([j for j in range(colSize)], i)])
        # 조합들의 유일성 검증
        for comb in all:
            #set에 추가하여 사이즈 비교로 검증
            vaildSet = set()
            # 조합에 해당되는 로우를 하나의 str로 합쳐서 set에 넣음
            for row in range(rowSize):
                temp = ''
                for col in comb:
                    temp += relation[row][col]
                vaildSet.add(temp)
            # 유일성 확인하여 리스트에 추가
            if len(vaildSet) == rowSize:
                uniqeIndex.append(comb)
        print(uniqeIndex)

solution(relation)

