def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    i = 0
    while i < len(intervals) - 1:
        if intervals[i][1] >= intervals[i+1][0]:
            intervals[i] = [intervals[i][0], max(
                intervals[i][1], intervals[i+1][1])]
            intervals.pop(i + 1)
        else:
            i += 1

    return intervals


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))
