food_times = [2,1,3]
k = 4

def solution(food_times, k):
    time = 0
    while True:
        for i in range(len(food_times)):
            if time == k:
                if sum(food_times) == 0:
                    answer = -1
                else:
                    answer = i + 1
                return answer
            if food_times[i] != 0:
                food_times[i] = food_times[i] - 1
                time += 1


print(solution(food_times,k))