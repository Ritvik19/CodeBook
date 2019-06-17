for i in range(int(input())):
	s = input()
	mx = 0
	for i in range(0,len(s)):
		count = 0
		for j in range(0,len(s)):
			if s[i]==s[j]:
				count+=1
		if count>mx:
			mx = count
	if len(s)-mx == mx:
		print("YES")
	else:
		print("NO")
