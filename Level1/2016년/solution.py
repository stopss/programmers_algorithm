def solution(a, b):
    answer = 0
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(a-1):
        answer += month[i]

    answer += b-1

    return date[answer%7]

# return days[(sum(months[:a-1])+b-1)%7]

