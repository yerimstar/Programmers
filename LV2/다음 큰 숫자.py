def solution(n):
    cnt = str(bin(n)[2:]).count('1')
    num = n+1
    while cnt != str(bin(num)[2:]).count('1'):
        num += 1
    return num

print(solution(78))