def solution(n):
    cnt = 0
    end = 0
    interval_sum = 0
    data = [_ for _ in range(1,n+1)]
    for start in range(n):
        while interval_sum < n and end < n:
            interval_sum += data[end]
            end += 1
        if interval_sum == n:
            cnt += 1
        interval_sum -= data[start]
    return cnt

print(solution(15))