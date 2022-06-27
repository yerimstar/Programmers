import itertools
def solution(numbers):
    num = set(itertools.combinations(numbers,2))
    answer = list(set([n[0] + n[1] for n in num]))
    return sorted(answer)
numbers = [2,1,3,4,1]
solution(numbers)