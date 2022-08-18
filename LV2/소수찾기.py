'''
만들 수 있는 모든 수의 조합
-> 소수 검사
'''
from itertools import permutations

def is_primenumber(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    numbers_lst = []
    # 최대 7 (7이하 문자열)
    for i in range(1, len(numbers) + 1):
        numbers_lst.extend(set(list(permutations(numbers, i))))

    result = []
    for number in numbers_lst:
        num = int(''.join(number))
        if num not in result and num >= 2 and is_primenumber(num):
            result.append(num)

    return len(result)
