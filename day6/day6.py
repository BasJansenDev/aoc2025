import math

def part1():
    input = open('input').read().strip().split('\n')
    numbers = [list(line.split()) for line in input][:-1]
    symbols = [c for c in input[-1] if not c.isspace()]
    res = 0
    width = len(numbers[0])
    for j in range(0,width):
        parsed = [int(p[j]) for p in numbers]
        if symbols[j] == '*':
            res += math.prod(parsed)
        else:
            res += sum(parsed)
    return res

def part2():
    input = open('input').read().split('\n')
    numbers = input[:-1]
    symbols = [c for c in input[-1] if not c.isspace()]
    count,res = 0,0
    parsed = []
    width = len(numbers[0])
    for i in range(0,width):
        number = ''.join(row[i] for row in numbers).strip()
        if number:
            parsed.append(int(number))
        if not number or i == width-1:
            if symbols[count] == '*':
                res += math.prod(parsed)
            else:
                res += sum(parsed)
            count += 1
            parsed = []
    return res

print(part1())
print(part2())