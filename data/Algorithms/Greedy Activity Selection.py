def greedyActivitySelection(intervals):
    intervals = list(sorted(intervals, key=lambda x: x[1]))
    activities = [intervals[0]]
    i = 0
    for j in range(1, len(intervals)):
        if intervals[j][0] > intervals[i][1]:
            activities.append(intervals[j])
            i = j
    return activities

if __name__ == '__main__':
    intervals = [(1,2), (3,4), (0,6), (5,7), (8,9), (5, 9)]
    print(*greedyActivitySelection(intervals), sep="\n")