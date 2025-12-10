from collections import deque

def part1():
    lines = open('input').read().strip().split('\n')
    res = 0
    for i in range(len(lines)):
        print("Handling line " + str(i) + " out of " + str(len(lines)))
        l = lines[i].split(' ')
        output = list(l[0].strip("[]"))
        initial = ('.') * len(output)
        buttons = [list(map(int, p.strip("()").split(","))) for p in l[1:-1] if p.startswith("(")]
        res += bfs(initial,buttons,output)
    return res

def bfs(initial,buttons,result):
    start = tuple(initial)
    goal = tuple(result)

    if start == goal:
        return 0

    q = deque()
    q.append((start, 0))
    visited = {start}

    while q:
        state, depth = q.popleft()

        for button in buttons:
            new_states = list(state)
            for idx in button:
                new_states[idx] = '#' if new_states[idx] == '.' else '.'
            new_state = tuple(new_states)

            if new_state == goal:
                return depth + 1

            if new_state not in visited:
                visited.add(new_state)
                q.append((new_state, depth + 1))

def part2():
    lines = open('input').read().strip().split('\n')
    res = 0
    for i in range(len(lines)):
        print("Handling line " + str(i) + " out of " + str(len(lines)))
        l = lines[i].split(' ')
        output = list(map(int, l[-1].strip("{}").replace(" ", "").split(",")))
        buttons = [list(map(int, p.strip("()").split(","))) for p in l[1:-1] if p.startswith("(")]
        res += search(buttons, output)
    return res

def search(buttons, output):
    pass

print(part1())
print(part2())