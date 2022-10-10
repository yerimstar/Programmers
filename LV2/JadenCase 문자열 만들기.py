def solution(s):
    # 공백 기준으로 단어 자르기
    words = s.split(' ')
    answer = ''
    for i in range(len(words)):
        # 공백이 추가로 나오는 경우
        if words[i] == '':
            answer += ' '
            continue
        # 공백 기준으로 잘랐기 때문에 다시 공백 추가
        if not i == 0:
            answer += ' '
        # 첫 문자가 숫자라면 그대로
        if words[i][0].isdigit():
            answer += words[i][0]
        # 첫 문자가 알파벳이라면 대문자 변환
        else:
            answer += words[i][0].upper()
        # 나머지 문자는 소문자 처리
        answer += words[i][1:].lower()
    return answer

solution("3people unFollowed me")