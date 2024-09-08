def solution(line):
    answer = []
    xs = []
    ys = []
    
    # 교점 찾기
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            div_under = line[i][0]*line[j][1] - line[i][1]*line[j][0]
            if div_under != 0:
                x = (line[i][1]*line[j][2] - line[i][2]*line[j][1])/ div_under
                y = (line[i][2]*line[j][0] - line[i][0]*line[j][2])/ div_under
                if int(x) == x and int(y) == y:
                    xs.append(int(x))
                    ys.append(int(y))
    x_max, x_min = max(xs), min(xs)
    y_max, y_min = max(ys), min(ys)
    
    # 좌표 찍기
    board = [["." for _ in range(x_max-x_min+1)] for _ in range(y_max-y_min+1)] # 좌표평면
    
    for x, y in zip(xs, ys):
        board[y_max-y][x-x_min] = "*"
    
    # xs = map(lambda x: x-x_min, xs)
    # ys = map(lambda y: -(y-y_max), ys)
    # for x, y in zip(xs, ys):
    #     board[y][x] = "*"

    for row in board:
        answer.append("".join(row))
    return answer