def solution(board, moves):
    tmp = []
    answer = 0
    for move in moves:
        for b in board:
            if b[move-1] != 0:
                if len(tmp) == 0:
                    tmp.append(b[move-1])
                else:
                    if tmp[-1] == b[move - 1]:  # 같은 인형인 경우 터뜨리기
                        answer += 2
                        tmp.pop(-1)  # 기존에 있던 인형 없애기
                    else:  # 같은 인형이 아닌 경우 인형 추가
                        tmp.append(b[move - 1])
                b[move-1] = 0
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board,moves)