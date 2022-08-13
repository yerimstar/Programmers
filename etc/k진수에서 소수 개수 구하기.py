import math

def prime_number(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0

    # n진수 변환
    number = ""
    while n > 0:
        n, mod = divmod(n,k)
        number += str(mod)

    number = [x for x in " ".join(number[::-1].split("0")).split() if int(x) >= 2]

    for n in number:
        if prime_number(int(n)):
            answer += 1
    return answer

n = 221020102030
k = 10
answer = solution(n,k)
print(answer)