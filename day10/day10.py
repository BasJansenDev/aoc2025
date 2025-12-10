import pulp
from collections import deque


def main(part1):
    lines = open('input').read().strip().split('\n')
    res = 0
    for i in range(len(lines)):
        l = lines[i].split(' ')
        buttons = [list(map(int, p.strip("()").split(","))) for p in l[1:-1] if p.startswith("(")]
        if(part1):
          output = tuple(l[0].strip("[]"))
          initial = tuple(('.') * len(output))
          res += bfs(initial,buttons,output)
        else:
          output = tuple(map(int, l[-1].strip("{}").split(",")))
          n = len(output)
          vectors = []
          for button in buttons:
              arr = [1 if j in button else 0 for j in range(n)]
              vectors.append(arr)
          res += sum(solve_line_with_pulp(vectors, output, i))
    return res

def bfs(initial,buttons,result):
    q = deque()
    q.append((initial, 0))
    visited = {initial}

    while q:
        state, depth = q.popleft()

        for button in buttons:
            new_states = list(state)
            for idx in button:
                new_states[idx] = '#' if new_states[idx] == '.' else '.'
            new_state = tuple(new_states)

            if new_state == result:
                return depth + 1

            if new_state not in visited:
                visited.add(new_state)
                q.append((new_state, depth + 1))

def solve_line_with_pulp(vectors, output, line_idx):
    model = pulp.LpProblem(f"line_{line_idx}", pulp.LpMinimize)
    k = [
        pulp.LpVariable(f"k_{j}", lowBound=0, cat="Integer")
        for j in range(len(vectors))
    ]
    for i in range(len(output)):
        model += (
            pulp.lpSum(k[j] * vectors[j][i] for j in range(len(vectors))) == output[i],
            f"pos_{i}"
        )
    model += pulp.lpSum(k), "total_presses"
    status = model.solve(pulp.PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[status] != "Optimal":
        return None
    presses = [int(var.value()) for var in k]
    return presses


print(main(True))
print(main(False))
