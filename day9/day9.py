def main():
    lines = open('input').read().split('\n')
    res = 0
    for i in range(0,len(lines)):
        for j in range(i+1,len(lines)):
            x1,y1 = lines[i].split(',')
            x2,y2 = lines[j].split(',')
            res = max(res, abs(int(x1)-int(x2)+1)*abs(int(y1)-int(y2)+1))
    return res

def no_point_between(p1, p2, points):
    x1, y1 = p1
    x3, y3 = p2
    min_x, max_x = min(x1, x3), max(x1, x3)
    min_y, max_y = min(y1, y3), max(y1, y3)

    return not any(
        min_x < x < max_x and min_y < y < max_y
        for x, y in points
    )

def main2():
    lines = open('testinput').read().split('\n')
    points = [tuple(map(int, line.split(','))) for line in lines]
    res = 0
    for i in range(0,len(points)-1):
        for j in range(i+2,len(points)-1):
            x1,y1 = points[i]
            x2,y2 = points[i+1]
            x3,y3 = points[j]
            x4,y4 = points[j+1]

            if (y1 == y2 and x2 == x3 and ((x2 >= x1 >= x4) or (x2 <= x1 <= x4))) or (x1 == x2 and y2 == y3 and ((y2 >= y1 >= y4) or (y2 <= y1 <= y4))):
                if(no_point_between(points[i],points[j],points)):
                    res = max(res, (abs(x1-x3)+1)*(abs(y1-y3)+1))
                    print("Values: " + str([x1,y1]) + " and " + str([x2,y2]) + " and " + str([x3,y3]) + " and "+ str([x4,y4]))

    return res


print(main())
print(main2())