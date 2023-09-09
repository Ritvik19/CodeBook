# O(n log n) O(1)

def minimumWaitingTime(queries):
    waiting_time = 0
    queries.sort()
    for i, w in enumerate(queries):
        waiting_time += w * (len(queries) - (i + 1))
    return waiting_time

minimumWaitingTime(**{
  "queries": [3, 2, 1, 2, 6]
})