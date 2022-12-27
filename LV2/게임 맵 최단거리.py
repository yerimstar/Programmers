from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    move = [[0,1],[0,-1],[1,0],[-1,0]]
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        for mx,my in move:
            dx = x + mx
            dy = y + my
            if 0 <= dx < n and 0 <= dy < m:
                if not visited[dx][dy] and maps[dx][dy] == 1:
                    visited[dx][dy] = visited[x][y] + 1
                    q.append((dx,dy))
    if visited[-1][-1] != 0:
        answer = visited[-1][-1]
    else:
        answer = -1
    return answer