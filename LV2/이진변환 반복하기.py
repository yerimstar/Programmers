def solution(s):
    cnt = 0
    zero = 0
    while s != '1':
        cnt += 1
        zero += len(s) - s.count('1')
        # 모든 0 제거
        s = '1' * s.count('1')
        # 문자열의 길이를 이진수로 변환
        s = str(bin(len(s))[2:])
    lst = [cnt,zero]
    return lst

print(solution("110010101001"))