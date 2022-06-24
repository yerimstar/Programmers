def solution(s):
    dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
            'nine': 9}
    if not s.isdigit():
        answer = ""
        tmp = ""
        for i in range(len(s)):
            if not s[i].isdigit():
                tmp += s[i]
                if tmp in dict.keys():
                    val = dict[tmp]
                    answer += str(val)
                    tmp = ""
            else:
                answer += s[i]
    else:
        answer = s

    return int(answer)

s = "one4seveneight"
solution(s)