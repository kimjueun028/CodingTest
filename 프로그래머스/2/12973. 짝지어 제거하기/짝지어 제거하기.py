def solution(s):
    stack = []
    for i in s:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return 0 if stack else 1

    # new_s = list(s)
    # i = 0
    # len_s = len(s)
    # while i <= (len_s-2):
    #     n, m = new_s[i:i+2]
    #     if n == m:
    #         new_s[i:i+2] = []
    #         len_s -= 2
    #         i -= 1 if i else 0
    #         continue
    #     i += 1
    # return 0 if len_s else 1