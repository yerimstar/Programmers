def ryan(n,info,value):
    tmp = []
    for i in range(len(info)):
        if i < value:
            tmp.append(0)
            continue

        if n > 0:
            if n >= info[i] + 1:
                tmp.append(info[i] + 1)
                n -= (info[i] + 1)
            else:
                tmp.append(0)
        else:
            tmp.append(0)
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

    for i in range(11):
        tmp = ryan(n,info,i)
        print(tmp)
        appeach_score,ryan_score = arrow_sum(info,tmp)
        print(ryan_score,appeach_score)
        if tmp in answer.values():
            answer = [-1]
            return answer
        answer[ryan_score-appeach_score] = tmp

    print(answer)
    answer = sorted(answer.items() ,key=lambda x : x[0],reverse = True)[0][1]
    return answer

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
answer = solution(n,info)
print(answer)