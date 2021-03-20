# solution

n, edge = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
result = 3

def graph_preprocess(arr):
    graph = {}
    for i in arr:
        if i[0] not in graph:
            graph[i[0]] = {i[1]}
        else:
            graph[i[0]].add(i[1])
        if i[1] not in graph:
            graph[i[1]] = {i[0]}
        else:
            graph[i[1]].add(i[0])
    return graph

def max_dist_num(dist):
    num = 0
    mxn = 0
    for i in dist:
        if dist[i] > mxn:
            num = 1
            mxn = dist[i]
        elif dist[i] == mxn:
            num += 1
    return num


import heapq

def solution(n, edge):
    graph = graph_preprocess(edge)
    dist = {node:float('inf') for node in graph}
    dist[1] = 0
    queue = []
    heapq.heappush(queue, [dist[1], 1])
    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_dist > dist[current_node]:
                continue
        for next_node in graph[current_node]:
            total_dist = 1 + current_dist

            if total_dist < dist[next_node]:
                dist[next_node] = total_dist
                heapq.heappush(queue, [total_dist, next_node])
    answer = max_dist_num(dist)
    return answer


print(solution(n, edge))
'''
Dijkstra 알고리즘으로 풀었음

문제 설명
n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

제한사항
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
입출력 예
n	vertex	return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
입출력 예 설명
예제의 그래프를 표현하면 아래 그림과 같고, 1번 노드에서 가장 멀리 떨어진 노드는 4,5,6번 노드입니다.
'''
