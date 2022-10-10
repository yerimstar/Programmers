def solution(s):
    # 공백 기준으로 단어 자르기
    words = s.split(' ')
    answer = ''
    for word in words:
        if word[0].isalpha():
            answer += word[0].upper()
        else:
            answer += word[0]
        answer += word[1:].lower() + ' '
solution("3people unFollowed me")