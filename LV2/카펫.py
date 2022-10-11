import math
def solution(brown, yellow):
    x = int((-(4-brown) + math.sqrt((4-brown)**2-16*yellow))//4)
    y = int(yellow//x)
    answer = [x+2,y+2]
    return answer

solution(24,24)