def solution(participant, completion):
    for c in completion:
        if c in completion:
            participant.remove(c)
    return participant[0]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
solution(participant,completion)