def solution(brown, yellow):
    grid = brown + yellow
    for c in range(3, grid):
        if not grid % c:
            r = grid//c
            if (c-2)*(r-2) == yellow:
                return [r,c]