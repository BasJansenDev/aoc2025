from functools import lru_cache

@lru_cache(maxsize=None)
def dfs(node, dac, fft):
    if node == 'dac':
        dac = True
    if node == 'fft':
        fft = True
    if node == 'out':
        return 1 if (dac and fft) else 0
    total = 0
    for nxt in connections[node]:
        total += dfs(nxt, dac, fft)
    return total

def main(part1):
    lines = open('input').read().strip().split('\n')
    global connections
    connections = dict()
    for l in lines:
        entry,out = l.split(':')
        connections[entry] = out.strip().split(' ')
    return dfs('you' if part1 else 'svr',part1, part1)

print(main(True))
print(main(False))
