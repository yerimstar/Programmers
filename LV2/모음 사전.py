from itertools import product
def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    lst = []
    for i in range(5, 0, -1):
        lst += list(product(alpha, repeat=i))
    lst.sort()
    cnt = 1
    for l in lst:
        if word == ''.join(l):
            return cnt
        cnt += 1

