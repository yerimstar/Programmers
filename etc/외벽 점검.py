import itertools

def solution(n, weak, dist):
    answer = 99999 # 최솟값 업데이트
    distList = list(itertools.permutations(dist,len(dist)))
    weaksize = len(weak)
    weak = weak + [w + n for w in weak]
    for i in range(weaksize):
        for dist in distList:
            cnt = 1
            start = i
            for j in range(1, weaksize):
                next = i + j
                diff = weak[next] - weak[start] # 사이 간격
                if diff > dist[cnt-1]:
                    cnt += 1
                    start = next
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                answer = min(answer,cnt)
    if answer == 99999:
        return -1
    return answer

n = 12
weak = [1, 3, 4, 9, 10]
dist = [3,5,7]
solution(n,weak,dist)