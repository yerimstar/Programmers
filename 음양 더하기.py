def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    answer = sum(absolutes)
    return answer

absolultes = [4,7,12]
signs = [True,False,True]
solution(absolultes,signs)