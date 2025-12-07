from collections import defaultdict

def main(part1):
    matrix = [list(row) for row in open('input').read().split('\n')]
    height, width = len(matrix), len(matrix[0])
    res1, res2 = 0, 0
    dp = defaultdict(int)
    dp[1,matrix[0].index('S')] = 1
    for i in range(1, height):
        for j in range(0, width):
            if (i-1, j) in dp:
                if matrix[i][j] == '^':
                    dp[i,j-1] += dp[i-1,j]
                    dp[i,j+1] += dp[i-1,j]
                    res1 += 1
                else:
                    dp[i,j] += dp[i-1,j]
    for i in range(0,width):
        res2 += dp[height-1,i]
    if part1:
        return res1
    else:
        return res2

print(main(True))
print(main(False))