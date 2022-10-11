def solution(n):
    cnt = 0
    end = 0
    interval_sum = 0
    # 1부터 n+1까지의 숫자 배열 생성
    data = [_ for _ in range(1,n+1)]
    # start를 0부터 이동
    for start in range(n):
        # 현재 합이 n보다 작고 end값이 n보다 작다면, end를 증가시키면서 합을 늘려준다.
        while interval_sum < n and end < n:
            interval_sum += data[end]
            end += 1
        # 현재 합이 n과 같다면 연속하는 자연수의 합을 찾은 것이기 때문에 cnt값을 증가시킨다.
        if interval_sum == n:
            cnt += 1
        # start값이 증가되면 현재 합이 감소해야 하므로 start위치에 있는 값을 현재 합에서 빼준다.
        interval_sum -= data[start]
    return cnt

print(solution(15))