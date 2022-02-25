def rotate(key,k):
    n = len(key)
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if k == 0: # 기본
                tmp[i][j] = key[i][j]
            else: # 90도 회전
                tmp[j][n-i-1] = key[i][j]
    return tmp

def check(arr,n,offset):
    for i in range(n):
        for j in range(n):
            if arr[offset+i][offset+j] != 1:
                return False
    return True

def solution(key, lock):
    offset = len(key) - 1 # 자물쇠와 열쇠가 최소 하나는 겹쳐야 함
    for i in range(4): # 회전
        key = rotate(key,i) # key 배열 회전
        for j in range(offset + len(lock)):
            for k in range(offset + len(lock)):
                arr = [[0 for _ in range(offset*2 + len(lock))] for _ in range(offset*2 + len(lock))] # 빈 배열
                for a in range(len(lock)):
                    for b in range(len(lock)):
                        arr[offset+a][offset+b] = lock[a][b]# 자물쇠 복사
                for a in range(len(key)):
                    for b in range(len(key)):
                        arr[a + k][b + j] += key[a][b]  # 키 값 합치기
                if check(arr,len(lock),offset) == True: # 자물쇠의 홈과 돌기가 모두 맞는지 확인
                    return True
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))