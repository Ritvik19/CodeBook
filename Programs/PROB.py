for t in range(int(input())):
	win, lose, retry, drop = map(int, input().split())
	w = float(win)
	l = float(lose)
	print(w / (w + l))
