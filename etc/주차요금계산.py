import math

def solution(fees, records):
    parking = {}
    time = {}
    for r in records:
        r = r.split(" ")
        t = int(r[0].split(":")[0]) * 60 + int(r[0].split(":")[1])
        if r[1] not in time.keys():
            time[r[1]] = 0
        else:
            if r[2] == 'OUT':
                time[r[1]] += (t-parking[r[1]][0])
        parking[r[1]] = ((t, r[2]))

    for k,v in parking.items():
        if v[1] == 'IN':
            time[k] += (1439-v[0])

    time = sorted(time.items(), key = lambda x : x[0])
    answer = []
    for t in time:
        if t[1] > fees[0]:
            money = fees[1] + math.ceil((t[1]-fees[0])/fees[2]) * fees[3]
        else:
            money = fees[1]
        answer.append(money)

    return answer

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
answer = solution(fees,records)
print(answer)