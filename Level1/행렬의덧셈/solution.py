def solution(a, b):
    answer = []
    for i in range(len(a)):
        temp = []
        for j in range(len(a[0])):
            temp.append(a[i][j] + b[i][j])
        answer.append(temp)

    return answer

