def possible(answer): # 구조물이 가능한지 확인하는 함수
    for x,y,a in answer:
        if a == 0: # 기둥
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif a == 1: # 보
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n,build_frame):
    answer = []
    for frame in build_frame:
        x,y,a,b = frame
        if b == 0: # 삭제하는 경우
            answer.remove([x,y,a])
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x,y,a]) # 다시 설치
        if b == 1: # 설치하는 경우
            answer.append([x,y,a])
            if not possible(answer):
                answer.remove([x,y,a]) # 가능한 구조물이 아니면 제거
    return sorted(answer)

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n,build_frame))