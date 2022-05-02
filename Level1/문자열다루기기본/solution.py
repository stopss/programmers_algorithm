def solution1(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False

# 한 줄 코드
def solution2(s):

    return True if (len(s) == 4 or len(s) == 6) and s.isdigit() else False
