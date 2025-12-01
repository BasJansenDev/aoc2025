def main1():
    input =  open('input').read().split('\n')
    counter = 50
    res = 0
    for i in input:
        val = int(i[1:])
        counter += -val if i.startswith('L') else val
        counter %= 100
        if(counter == 0):
            res += 1
    return res

def main2():
    input = open('input').read().split('\n')
    counter = 50
    res = 0
    for i in input:
        val = int(i[1:])
        oldVal = counter
        res += val // 100
        val %= 100
        counter += -val if i.startswith('L') else val
        if(counter >= 100 or counter <= 0 and oldVal != 0):
            res +=1
        counter %= 100

    return res

print(main1())
print(main2())
