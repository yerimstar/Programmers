from itertools import permutations
def solution(k, dungeons):
    lst = list(permutations(dungeons,len(dungeons)))
    result = 0
    for dungeon in lst:
        now = k
        cnt = 0
        for d in dungeon:
            if now >= d[0]:
                now -= d[1]
                cnt += 1
        result = max(result,cnt)
    return result