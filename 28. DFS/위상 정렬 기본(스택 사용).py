"""
출처 : https://sexy-developer.tistory.com/56

알고리즘
1. 모든 정점의 진입 차수를 계산
2. 진입 차수가 0인 정점을 스택에 삽입
3. 위성 순서를 생성
"""
adj_list = {0:[2,3], 1:[3,4], 2:[3,5], 3:[5], 4:[5], 5:[]} #인접 리스트

def topological_sort_stack(adj_list):
    in_degree = [0] * len(adj_list)
    stack = []
    answer = []

    #1. 모든 정점의 진입 차수를 계산
    for i in range(len(adj_list)): #0~5
        for j in range(len(adj_list)): #0~5
            temp = adj_list[j] #value 값인 "리스트"를 받는다. 처음엔 [2,3]을 받는다.
            for k in range(len(temp)):
                if temp[k] == i:
                    in_degree[i] += 1 #이 노드는 "위상이 1 증가한다."
    print("in_degree 배열 :",in_degree)

    #2. 진입 차수가 0인 정점을 스택에 삽입
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            stack.append(i)
    print("초기 스택:",stack)

    #3. 위상 순서를 생성
    while stack:
        node = stack.pop() #현재 위상 삭제
        answer.append(node) 

        for i in range(len(adj_list[node])): #인접 위상 탐색
            idx = adj_list[node][i]
            in_degree[idx] -= 1
            if in_degree[idx] == 0:
                stack.append(idx)
