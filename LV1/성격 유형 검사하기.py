def solution(survey, choices):
    score = [3, 2, 1, 0, 1, 2, 3]
    dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i, choice in enumerate(choices):
        if choice <= 3:
            dict[survey[i][0]] += score[choice - 1]
        elif choice >= 5:
            dict[survey[i][1]] += score[choice - 1]

    answer = ''
    if dict['R'] >= dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dict['C'] >= dict['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dict['J'] >= dict['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dict['A'] >= dict['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer