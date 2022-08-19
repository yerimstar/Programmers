def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    same = lost & reserve
    answer = n - len(lost) + len(same)
    lost = lost - same
    reserve = list(reserve - same)
    for l in lost:
        for r in reserve:
            if l - 1 <= r <= l + 1:
                answer += 1
                reserve.remove(r)

    return answer