import itertools

def ryan(n,ryan,appeach):
    tmp = []
    for i in range(11):
        if ryan[i] == 1:
            n -= (appeach[i] + 1)
            tmp.append(appeach[i]+1)
        else:
            if i == 10 and n > 0:
                tmp.append(n)
            else:
                tmp.append(0)

        if n < 0:
            tmp = []
            return tmp
    return tmp

def arrow_sum(appeach,ryan):
    appeach_score = 0
    ryan_score = 0
    for i in range(11):
        if appeach[i] == 0 and ryan[i] == 0:
            continue

        if appeach[i] >= ryan[i]:
            appeach_score += (10 - i)
        else:
            ryan_score += (10 - i)

    return appeach_score,ryan_score

def solution(n, info):
    answer = {}
    choice = [1,0]
    result = list(itertools.product(choice,repeat = 11)) # 중복순열
    for r in result:
        tmp = ryan(n,r,info)
        if tmp:
            appeach_score, ryan_score = arrow_sum(info, tmp)
            answer[ryan_score-appeach_score] = tmp

    answer = sorted(answer.items(), key=lambda x: x[0], reverse=True)[0]
    if answer[0] < 0:
        answer = [-1]
    else:
        answer = answer[1]

    return answer

n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
answer = solution(n,info)
print(answer)