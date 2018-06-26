def solve(a, b, c, d):
	if a>b or c>d or d<a:
		return 0

	if b>d:
		b = d
	if c<a:
		c= a

	if b<c:
		return (b-a+1)*(d-c+1)

	ans = (b-a+1)*(d-c+1)
	ans -= (b-c+1)*(b-c+2)//2

	return ans

for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    n1 = b-a+1
    n2 = d-c+1
    print(solve(a, b, c, d))
