def calculate_gaps(values):
    temp = []
    gaps = []
    n = len(values)
    gap = 1
    i = 2
    while gap < n:
        temp.append(gap)
        gap = (2 ** i) - 1
        i += 1
    for i in range(len(temp) - 1, -1, -1):
        gaps.append(temp[i])
    return gaps

def sort(values):
    n = len(values)
    gaps = calculate_gaps(values)
    for gap in gaps:
        for i in range(gap, n):
            temp = values[i]
            j = i
            while j >= gap and values[j - gap] > temp:
                values[j] = values[j - gap]
                j -= gap
            values[j] = temp

values = [5, 2, 9, 1, 5, 6]

sort(values)

print(calculate_gaps(values))
print((values))