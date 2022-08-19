from collections import defaultdict, deque


def bfs(cut, n, graph):
    count = 0
    queue = deque()
    visited = [0 for _ in range(n)]
    # 시작 노드
    queue.append(cut[0])
    visited[cut[0]] = True
    while queue:
        node = queue.popleft()
        for nd in graph[node]:
            print(nd)
            if not visited[nd] and nd != cut[1]:
                queue.append(nd)
                visited[nd] = True
                count += 1
    return count


def solution(n, wires):
    graph = defaultdict(set)
    for a, b in wires:
        graph[a].add(b)
        graph[b].add(a)

    for w in wires:
        print(w)
        cnt = bfs(w, n, graph)
        print(cnt)

solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])