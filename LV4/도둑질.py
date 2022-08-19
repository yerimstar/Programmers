def solution(money):
    # 돈의 수
    n = len(money)

    # 집이 원형모양으로 존재하기 때문에 첫 번째를 무시하는 경우와 마지막을 무시하는 경우를 나눠서 계산해야 한다.
    # 첫 번째를 무시하는 경우
    d1 = [0] * (n)
    d1[0] = 0
    d1[1] = money[1]
    d1[2] = money[2]
    for i in range(3, n):
        d1[i] = max(d1[i - 3] + money[i], d1[i - 2] + money[i])
    answer1 = max(d1)
    # 마지막을 무시하는 경우
    d2 = [0] * (n)
    d2[0] = money[0]
    d2[1] = money[1]
    d2[2] = money[0] + money[2]
    for i in range(3, n - 1):
        d2[i] = max(d2[i - 3] + money[i], d2[i - 2] + money[i])
    answer2 = max(d2)
    # 두 값 중 더 큰 값을 최댓값이라고 본다
    answer = max(answer1, answer2)
    return answer

