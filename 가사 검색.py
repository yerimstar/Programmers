words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def solution(words, queries):
    answer = []
    for query in queries:
        check = 0
        wild_cnt = query.count('?')  # ? 길이
        same_cnt = len(query) - wild_cnt  # 일치하는 문자의 길이
        start = 'a' * wild_cnt
        end = 'z' * wild_cnt

        if query[0] == '?':  # 접두사인 경우
            new_words = [x[:wild_cnt] for x in words if len(query) == len(x) and query[-same_cnt:] == x[-same_cnt:]]
            new_words.sort()
            for word in new_words:
                if start <= word <= end:
                    check += 1
            answer.append(check)
        else:  # 접미사인 경우
            new_words = [x[-wild_cnt:] for x in words if len(query) == len(x) and query[:same_cnt] == x[:same_cnt]]
            new_words.sort()
            for word in new_words:
                if start <= word <= end:
                    check += 1
            answer.append(check)
    print(answer)
    return answer

solution(words,queries)




