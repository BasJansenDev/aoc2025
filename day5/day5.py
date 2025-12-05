def main():
    input = open('input').read().split('\n\n')
    ranges = input[0].split('\n')
    ingredients = input[1].split('\n')
    res = 0
    freshness = []
    for r in ranges:
        freshness += [list(map(int,r.split('-')))]
    for ingredient in ingredients:
        for fresh in freshness:
            if int(ingredient) >= fresh[0] and int(ingredient) <= fresh[1]:
                res += 1
                break
    return res

def mergeRanges(result):
    result.sort(key=lambda x: x[0])
    merged = [result[0]]
    for start, end in result[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged

def main2():
    ranges = open('input').read().split('\n\n')[0].split('\n')
    result = []
    for r in ranges:
        result.append(list(map(int, r.split('-'))))
    return sum(end - start + 1 for start, end in mergeRanges(result))

print(main())
print(main2())