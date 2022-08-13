import re
def solution(new_id):
    new_id = new_id.lower() # 1단계 - 소문자 치환
    new_id = re.sub(r'[^0-9a-z-_.]','',new_id) # 2단계 - 알파벳 소문자, 숫자, -, _ , . 제외 모든 문자 제거
    while '..' in new_id: # 3단계 - 마침표 2번이상 연속된 부분을 하나의 마침표로 치환
        new_id = new_id.replace('..','.')
    new_id = new_id.strip('.') # 4단계 - 마침표 맨 앞 맨 뒤일경우 제거
    if len(new_id) == 0: # 5단계 - 빈 문자열이라며, "a" 대입
        new_id = "a"
    if len(new_id) >= 16: # 6단계
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if len(new_id) == 2:
        new_id = new_id[0] + new_id[1] * 2
    elif len(new_id) == 1:
        new_id = new_id * 3
    answer = new_id
    return answer

new_id = "=.="
solution(new_id)