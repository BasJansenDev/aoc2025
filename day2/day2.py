def main(part1):
    input = open('input').read().split(',')
    res = 0
    for r in input:
        left,right = map(int,r.split('-'))
        for j in range(left,right+1):
            h = str(j)
            if part1 and h[len(h)//2:] == h[:len(h)//2]:
                res +=j
            if not part1:
                if h in (h + h)[1:-1]:
                    res += j
    return res

print(main(True))
print(main(False))