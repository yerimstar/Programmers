def solution(lottos, win_nums):
    min_score = 7-len(list(set(lottos).intersection(win_nums)))
    if min_score == 7:
        min_score = 6
    max_score = min_score - lottos.count(0)
    if max_score == 0:
        max_score = 1
    answer = [max_score,min_score]
    print(answer)
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums =[31, 10, 45, 1, 6, 19]
solution(lottos,win_nums)