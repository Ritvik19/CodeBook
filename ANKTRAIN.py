neighbour = ["7SL", "4LB", "5MB", "6UB", "1LB", "2MB", "3UB", "8SU"]
for i in range(int(input())):
    n = int(input())
    print(neighbour[n%8])
