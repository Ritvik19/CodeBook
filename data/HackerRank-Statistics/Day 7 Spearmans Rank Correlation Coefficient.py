# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input().strip())
X = [float(i) for i in input().strip().split(' ')]
Y = [float(i) for i in input().strip().split(' ')]

rankx = [sorted(X).index(X[i])+1 for i in range(N)]
ranky = [sorted(Y).index(Y[i])+1 for i in range(N)]

d_i_sq = [(rankx[i] - ranky[i])**2 for i in range(N)]
r_xy = 1- 6*sum(d_i_sq)/(N*(N**2-1))

print(round(r_xy, 3))
