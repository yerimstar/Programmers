def solution(id_list, report, k):
    # k는 몇 번 신고당했을 때 정지될지
    result = dict.fromkeys(id_list,0)
    result2 = dict.fromkeys(id_list,0)
    report = list(set(report)) # 여러번 신고 -> 1회로 간주함

    check = set()
    for r in report:
        result[r.split(" ")[1]] += 1
        if result[r.split(" ")[1]] >= k:
            check.add(r.split(" ")[1])

    for r in report:
        if r.split(" ")[0] in id_list and r.split(" ")[1] in check:
            result2[r.split(" ")[0]] += 1

    answer = list(result2.values())
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
answer = solution(id_list,report,k)
print(answer)

