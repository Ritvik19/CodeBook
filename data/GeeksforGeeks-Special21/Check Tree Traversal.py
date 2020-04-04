def checktree(preorder, inorder, postorder, length): 
	if length == 0: 
		return 1

	if length == 1: 
		return (preorder[0] == inorder[0]) and (inorder[0] == postorder[0])
		
	if preorder[0] != postorder[length-1]:
	    return 0

	idx = -1
	
	for i in range(length): 
		if inorder[i] == preorder[0]: 
			idx = i 
			break
	
	if idx == -1:
		return 0

	ret1 = checktree(preorder[1:], inorder, postorder, idx)
 
	ret2 = checktree(preorder[idx + 1:], inorder[idx + 1:], 
						postorder[idx:], length-idx-1)
	
	return (ret1 and ret2) 

if __name__ == "__main__": 
	t = int(input())
	for _ in range(t):
		n = int(input())
		preorder = list(map(int, input().strip().split()))
		inorder = list(map(int, input().strip().split()))
		postorder = list(map(int, input().strip().split()))

		if(checktree(preorder, inorder, postorder, n)):
			print("Yes") 
		else: 
			print("No") 