def solution(price, money, count):
    answer = sum(price*(i+1) for i in range(count))

    return answer-money if money < answer else 0
