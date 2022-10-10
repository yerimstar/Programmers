def solution(s):
    # 공백 기준으로 단어 자르기
    words = s.split(' ')
    print(words)
    answer = ''
    for word in words:
        if word == '':
            answer += ' '
            continue
        if word[0].isdigit():
            answer += word[0]
        else:
            answer += word[0].upper()
        answer += word[1:].lower() + ' '
    return answer.strip()
solution("3people unFollowed me")