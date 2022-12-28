def solution(s):
    i = 0
    while len(s) != 0:
        if i == len(s)-1:
            break
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            i = 0
        else:
            i += 1
    if len(s) == 0:
        answer = 1
    else:
        answer = 0
    print(answer)
solution("cdcd")