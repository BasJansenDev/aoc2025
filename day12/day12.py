import math
from functools import lru_cache

def main():
    lines = open('input').read().strip().split('\n\n')
    presents = lines[0:-1]
    sizes = lines[-1].split('\n')
    presents = [tuple(tuple(row) for row in present.split('\n')[1:]) for present in presents]
    res = 0
    for size in sizes:
        print("Testing size " + size)
        size, indices = size.split(':')
        indices = list(map(int, indices.split()))
        shapes = []
        for i, count in enumerate(indices):
            shapes.extend([presents[i]] * count)

        W,H = map(int,size.split('x'))
        # Does a naive solution already work?
        if(len(shapes)*3*3 <= W*H):
            res += 1
            continue

        # Even if I could stack all the #'s next to each other, can it even fit?
        needed_cells = sum(shape_area(s) for s in shapes)
        if needed_cells > W*H:
            continue

        # Sort by size, so the clunky ones come first.
        shapes.sort(key=shape_area, reverse=True)
        initial_state = tuple(0 for _ in range(H))
        res += dfs(tuple(shapes), initial_state,W ,H)
    return res

# Rotates and caches a given shape
@lru_cache(None)
def rotate_shape(shape):
    return tuple(zip(*shape[::-1]))

# Rotates, caches and returns all unique rotations for a given shape
@lru_cache(None)
def unique_rotations(shape):
    rots = []
    s = shape
    for _ in range(4):
        if s not in rots:
            rots.append(s)
        s = rotate_shape(s)
    return tuple(rots)

# Convert a shape to a bitmask for faster checking
@lru_cache(None)
def shape_to_masks(shape):
    h = len(shape)
    w = len(shape[0])
    rows = []
    for r in shape:
        mask = 0
        for c in r:
            mask = (mask << 1) | (1 if c == '#' else 0)
        rows.append(mask)
    return tuple(rows), h, w

# Find all rotations for a given bitmasked shape
@lru_cache(None)
def all_rot_masks(shape):
    return tuple(shape_to_masks(r) for r in unique_rotations(shape))

# Calculate the area of a shape
def shape_area(shape):
    return sum(row.count('#') for row in shape)

# Checking if a shape can be placed
def can_place(mask_rows, board, x, y):
    for i, m in enumerate(mask_rows):
        if board[y + i] & (m << x):
            return False
    return True

# Inserting a shape
def insert_shape(mask_rows, board, x, y):
    new_board = list(board)
    for i, m in enumerate(mask_rows):
        new_board[y + i] |= (m << x)
    return tuple(new_board)

# Using MRV to find the most constrained shape for faster pruning of branches.
def most_restricted_value(shapes, board, W, H, ):
    limit = 2
    best_i = None
    best_count = float('inf')
    best_placements = None

    for i, shape in enumerate(shapes):
        placements = []
        count = 0

        for mask_rows, shape_height, shape_width in all_rot_masks(shape):
            # Skip if it already doesn't fit
            if shape_height > W or shape_width > H:
                continue

            # Check only topleft corners to lessen unnecessary checks where the shape won't even fit
            for y in range(H - shape_height + 1):
                for x in range(W - shape_width + 1):
                    if can_place(mask_rows, board, x, y):
                        placements.append((mask_rows, x, y))
                        count += 1
                        if count >= limit or count >= best_count:
                            break
                if count >= limit or count >= best_count:
                    break

        # If a shape has no possibilities anymore, we can prune the entire branch
        if count == 0:
            return i, []

        if count < best_count:
            best_i = i
            best_count = count
            best_placements = placements

    return best_i, best_placements


@lru_cache(None)
def dfs(shapes, board, W, H):
    if not shapes:
        return True

    # Find most constrained shape to quickly prune out a lot of unnecessary branches.
    i, placements = most_restricted_value(shapes, board, W, H)
    if not placements:
        return False

    rest = shapes[:i] + shapes[i+1:]

    # Apply all possible
    for mask_rows, x, y in placements:
        new_board = insert_shape(mask_rows, board, x, y)
        if dfs(rest, new_board, W, H):
            return True

    return False


print(main())
