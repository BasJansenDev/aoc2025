import copy

directions = {(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(1,1),(1,-1),(-1,1)}

matrix = [list(row) for row in open('input').read().split('\n')]
height, width = len(matrix), len(matrix[0])

def adjacent_cells(idx):
    return [(idx[0] + dy, idx[1] + dx) for dy, dx in directions
                if 0 <= idx[0] + dy < height and 0 <= idx[1] + dx < width
                and matrix[idx[0] + dy][idx[1] + dx] == '@' ]

def main(part1):
    res = 0
    while(True):
        old_matrix = copy.deepcopy(matrix)
        for y in range(height):
            for x in range(width):
                if (matrix[y][x] == '@' and len(adjacent_cells((y, x))) < 4):
                    res += 1
                    if(not part1) : matrix[y][x] = 'x'
        if(old_matrix == matrix or part1):
            break
    return res

print(main(True))
print(main(False))