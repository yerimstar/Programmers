def solution(A,B):
    result = 0
    for _ in range(len(A)):
        a = min(A)
        b = max(B)
        result += a*b
        A.remove(a)
        B.remove(b)
    return result