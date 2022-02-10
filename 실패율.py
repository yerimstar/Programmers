def solution(N,stages):
    result = []
    stage = [stages.count(i+1) for i in range(N)]
    tmp = 0
    player = len(stages)
    for i in range(N):
        print(i)
        divide = player-tmp
        if divide != 0:
            result.append((i+1,stage[i]/(player-tmp)))
        else:
            result.append((i+1,0))
        tmp += stage[i]
    result.sort(key = lambda x : -x[1])
    answer = [x[0] for x in result]
    print(result)
    return answer

solution(4,[4,4,4,4,4])