def solution(rows, columns, queries):
    answer = []
    # for i in range(rows):
    #     for j in range(columns):
    #         board[i][j] = columns*i+j+1
    board = [[columns*i + j + 1 for j in range(columns)] for i in range(rows)]
    
    for x1, y1, x2, y2 in queries:
        keys = []
        keys.extend([(x1, y) for y in range(y1, y2)])   # x1, y1 -> x1, y2
        keys.extend([(x, y2) for x in range(x1, x2)])   # x1, y2 -> x2, y2
        keys.extend([(x2, y) for y in range(y2, y1, -1)])   # x2, y2 -> x2, y1
        keys.extend([(x, y1) for x in range(x1+1, x2+1)][::-1])   # x2, y1 -> x1, y1
        
        values = []
        for x, y in keys:
            values.append(board[x-1][y-1])
        
        values = [values[-1]] + values[:-1]
        for i in range(len(keys)):
            x = keys[i][0]
            y = keys[i][1]
            board[x-1][y-1] = values[i]     
        answer.append(min(values))
    return answer



