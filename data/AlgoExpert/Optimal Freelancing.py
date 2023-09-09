# O (n log n) O(1)

def optimalFreelancing(jobs):
    profit = 0
    jobs.sort(key=lambda x: x['payment'], reverse=True)
    timeline = [False] * 7
    for job in jobs:
        time = min(job['deadline'], 7)
        for time in reversed(range(time)):
            if not timeline[time]:
                timeline[time] = True
                profit += job['payment']
                break
    return profit
optimalFreelancing(**{
  "jobs": [
    {
      "deadline": 1,
      "payment": 1
    },
    {
      "deadline": 2,
      "payment": 2
    },
    {
      "deadline": 2,
      "payment": 1
    }
  ]
})