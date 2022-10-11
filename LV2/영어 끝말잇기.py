def solution(n, words):
    lst = [words[0]]
    for i in range(1,len(words)):
        # 이미 말했던 단어
        if words[i] in lst:
            break
        # 끝말잇기 안됨
        if words[i - 1][-1] != words[i][0]:
            break
        # 한 글자 단어
        if len(words[i]) == 1:
            break
        lst.append(words[i])
    cnt = len(lst)
    if len(words) == cnt:
        return [0, 0]
    else:
        cnt += 1
        a = cnt % n
        if a == 0:
            a = n
            b = cnt // n
        else:
            b = cnt // n + 1
        return [a, b]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))