def checktree(preorder, inorder, postorder, length): 
	if length == 0: 
		return True

	if length == 1: 
		return (preorder[0] == inorder[0]) and (inorder[0] == postorder[0])
		
	if preorder[0] != postorder[length-1]:
	    return False

	idx = -1
	
	for i in range(length): 
		if inorder[i] == preorder[0]: 
			idx = i 
			break
	
	if idx == -1:
		return False

	ret1 = checktree(preorder[1:], inorder, postorder, idx)

	ret2 = checktree(preorder[idx + 1:], inorder[idx + 1:], 
						postorder[idx:], length-idx-1)
	
	return (ret1 and ret2) 

if __name__ == "__main__": 
    preorder = [1, 2, 4, 5, 3]
    inorder = [4, 2, 5, 1, 3]
    postorder = [4, 5, 2, 3, 1]
    print(checktree(preorder, inorder, postorder, len(inorder)))