def solution(s):
    stack = []
    for i in s:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return 0 if stack else 1

# 틀림
#     new_s = list(s)
    
#     i = 0
#     len_s = len(s)
#     while i <= (len_s-2):
#         n = new_s[i]
#         m = new_s[i+1]
#         if n == m:
#             new_s.remove(n)
#             new_s.remove(m)
#             i = 0
#             len_s = len(new_s)
#             continue
#         i += 1
#     return 0 if len(new_s) else 1