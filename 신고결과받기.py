def solution(id_list, report, k):
    # k는 몇 번 신고당했을 때 정지될지
    result = {}
    result2 = {}
    report = list(set(report)) # 여러번 신고 -> 1회로 간주함
    for id in id_list:
        result[id] = 0
        result2[id] = 0
    for r in report:
        result[r.split(" ")[1]] += 1
    check = [id[0] for id in result.items() if id[1] >= k] # 정지된 ID

    for id in id_list:
        for r in report:
            user_id = r.split(" ")[0]
            declaration_id = r.split(" ")[1]
            if user_id == id and declaration_id in check:
                result2[id] += 1
    answer = list(result2.values())
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
answer = solution(id_list,report,k)
print(answer)

