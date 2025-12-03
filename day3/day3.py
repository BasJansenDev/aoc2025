def main(stackSize):
    input = open('input').read().split('\n')
    res = 0
    for bank in input:
        stack = []
        bank = str(bank)
        removals = len(bank) - stackSize
        for i in range(len(bank)):
            while len(stack) != 0 and removals != 0 and bank[i] > stack[-1]:
                stack.pop()
                removals -= 1
            stack.append(bank[i])
        res += int("".join(stack[0:stackSize]))
    return res

print(main(2))
print(main(12))