def main(part2):
    input = open('input').read().split('\n')
    counter = 50
    res = 0
    for i in input:
        oldVal = counter
        val = int(i[1:])
        if(part2):
            res += val // 100
            val %= 100
        counter += -val if i.startswith('L') else val
        if(part2 and (counter >= 100 or counter <= 0 and oldVal != 0)):
            res += 1
        counter %= 100
        if(not part2 and counter == 0):
            res += 1

    return res

print(main(False))
print(main(True))
