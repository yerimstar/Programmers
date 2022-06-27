'''
시간복잡도 - O(N) for문 사용 -> 효율성 테스트 실패
def solution(participant, completion):
    for c in completion:
        if c in completion:
            participant.remove(c)
    return participant[0]
'''
def solution(participant, completion):
    if len(set(participant)) != len(participant):

    else:
        answer = list(set(participant)-set(completion))[0]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
solution(participant,completion)