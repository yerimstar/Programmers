def solution(numbers, hand):
    keypad = [[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    answer = ''
    righthand = '#'
    lefthand = '*'
    for num in numbers:
        if num in keypad[0]:
            answer += 'L'
            lefthand = num
        elif num in keypad[2]:
            answer += 'R'
            righthand = num
        else:
            check = keypad[1].index(num)
            for i in range(3):
                if righthand in keypad[i]:
                    rightcheck = abs(keypad[i].index(righthand) - check)
                    if i != 1:
                        rightcheck += 1
                    break

            for i in range(3):
                if lefthand in keypad[i]:
                    leftcheck = abs(keypad[i].index(lefthand) - check)
                    if i != 1:
                        leftcheck += 1
                    break
            if rightcheck > leftcheck :
                lefthand = num
                answer += 'L'
            elif rightcheck < leftcheck:
                righthand = num
                answer += 'R'
            elif rightcheck == leftcheck:
                if hand == 'right':
                    righthand = num
                    answer += 'R'
                elif hand == 'left':
                    lefthand = num
                    answer += 'L'

    return answer
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
solution(numbers,hand)