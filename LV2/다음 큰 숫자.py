def solution(n):
    cnt = bin(n)[2:]
    num = n+1
    while cnt != bin(num)[2:]:
        num += 1
    return num

print(solution(78))