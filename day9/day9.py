from collections import defaultdict

def edge_crosses_rectangle(e1, e2, x1, y1, x2, y2):
    edgeX1, edgeY1 = e1
    edgeX2, edgeY2 = e2
    lowPointX,highPointX = sorted((x1, x2))
    lowPointY,highPointY = sorted((y1, y2))

    # vertical edge
    if edgeX1 == edgeX2:
        if not (lowPointX < edgeX1 < highPointX): # check if the edge is even going through the rectangle
            return False
        lowEdgeY, highEdgeY = sorted((edgeY1, edgeY2))
        overlap_low = max(lowEdgeY, lowPointY)
        overlap_high = min(highEdgeY, highPointY)
        return overlap_high > overlap_low

    # horizontal edge
    if edgeY1 == edgeY2:
        if not (lowPointY < edgeY1 < highPointY):
            return False
        lowEdgeX, highEdgeX = sorted((edgeX1, edgeX2))
        overlap_low = max(lowEdgeX, lowPointX)
        overlap_high = min(highEdgeX, highPointX)
        return overlap_high > overlap_low

    return False

# check if a given X and Y coordinate are on one of the boundary lines of the points
def is_on_boundary(x, y, points):
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]

        if x1 == x2 == x and min(y1, y2) <= y <= max(y1, y2) or y1 == y2 == y and min(x1, x2) <= x <= max(x1, x2):
            return True

    return False

# check if a given X and Y coordinate are either on the boundary lines of the points, or within these boundaries.
def is_in_body(x, y, points, intersections):
    if is_on_boundary(x, y, points):
        return True

    xs = intersections.get(y)
    if not xs:
        return False

    inside = False

    # Flip everytime we hit an edge until the edge is further to the right than x is
    for wx in xs:
        if x < wx:
            break
        inside = not inside

    return inside


def main(part1):
    lines = open('input').read().strip().split('\n')
    points = [tuple(map(int, line.split(','))) for line in lines]
    res = 0
    intersections = defaultdict(list)
    n = len(points)

    # Create intersections map to later quickly test if a point is within the space of the boundaries.
    # This is done by creating small vertical lines that are later used as indicators for whether a point is "in" or "out"
    edges = []
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]

        # Store edges for edge intersection detection later
        edges.append([(x1, y1), (x2, y2)])

        # If it's a vertical line, we include it so we can later scan per line to detect 'in' and 'out'
        if x1 == x2:
            ymin, ymax = sorted((y1, y2))
            for y in range(ymin, ymax):
                intersections[y].append(x1)

    # Sort the intersections so we can later use them from left to right
    for y in intersections:
        intersections[y].sort()

    for i in range(n-1):
        x1,y1 = points[i]
        for j in range(i+1,n):
            x2,y2 = points[j]

            # If part 1:
            if(part1):
                res = max(res, (abs(int(x1)-int(x2))+1)*(abs(int(y1)-int(y2))+1))
            else:

                # If part 2:
                # For each two points test if:
                # - Are the two other points either on the boundary, or within the body?
                # - Is the subsequent rectangle not intersected by any other edges?
                if is_in_body(x1,y2, points,intersections) and is_in_body(x2,y1,points,intersections):
                    for edge in edges:
                        edgeX, edgeY = edge
                        if(edge_crosses_rectangle(edgeX,edgeY,x1,y1,x2,y2)):
                            break
                    else:
                        res = max(res, (abs(int(x1)-int(x2))+1)*(abs(int(y1)-int(y2))+1))
    return res

print(main(True))
print(main(False))
