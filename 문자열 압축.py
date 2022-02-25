def solution(s):
    result = []
    for i in range(1,len(s)//2+1): # 문자열을 나눠보면 문자열 길이의 절반이상이 되는 경우는 의미가 없음을 알 수 있음
        tmp = []
        for j in range(0,len(s),i): # 1부터 해당 길이만큼 문자열을 잘라준다.
            tmp.append(s[j:j+i])
        print(tmp)
        arr = []
        cnt = 1
        for k in range(len(tmp)):
            if k < len(tmp)-1 and tmp[k] == tmp[k+1]:
                cnt += 1
            else:
                if cnt > 1:
                    arr.append(str(cnt) + tmp[k])
                    cnt = 1
                else:
                    arr.append(tmp[k])
            print(arr)
            if k == len(tmp)-1:
                result.append(len(''.join(arr)))
        print(result)
    answer = min(result)
    print(answer)
    return answer

solution("abcabcdede")