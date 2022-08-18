def solution(answers):
    math_1 = [1, 2, 3, 4, 5] * (len(answers) // 5 + 1)
    math_2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    math_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)
    answer = []
    ans_1 = 0
    ans_2 = 0
    ans_3 = 0
    # N
    for i in range(len(answers)):
        if math_1[i] == answers[i]:
            ans_1 += 1
        if math_2[i] == answers[i]:
            ans_2 += 1
        if math_3[i] == answers[i]:
            ans_3 += 1
    result = max(ans_1, ans_2, ans_3)

    if result == ans_1:
        answer.append(1)
    if result == ans_2:
        answer.append(2)
    if result == ans_3:
        answer.append(3)
    return answer


