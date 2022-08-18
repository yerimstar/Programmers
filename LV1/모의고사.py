def solution(answers):
    math_1 = [1, 2, 3, 4, 5]
    math_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0,0,0]
    answer = []

    for idx,ans in enumerate(answers):
        if ans == math_1[idx % 5]:
            score[0] += 1
        if ans == math_2[idx % 8]:
            score[1] += 1
        if ans == math_3[idx % 10]:
            score[2] += 1

    max_score = max(score)
    for idx,sc in enumerate(score):
        if sc == max_score:
            answer.append(idx+1)
    return answer


