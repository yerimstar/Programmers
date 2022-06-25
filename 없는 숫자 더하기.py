def solution(numbers):
    nums = [_ for _ in range(10)]
    answer = sum(list(set(nums) - set(numbers)))
    return answer

numbers = [5,8,4,0,6,7,9]
solution(numbers)