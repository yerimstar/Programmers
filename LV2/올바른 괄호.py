def solution(s):
    answer = True
    # 스택
    stack = []
    for check in s:
        if check == '(':
            stack.append('(')
        elif check == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                answer = False
    if len(stack) != 0:
        answer = False
    return answer