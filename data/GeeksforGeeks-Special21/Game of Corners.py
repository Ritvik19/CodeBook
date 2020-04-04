def ValidCorner(matrix): 
    rows = len(matrix)
    columns = len(matrix[0])
    if (rows == 0): 
        return False
  
    columns = len(matrix[0]) 

    table = {} 

    for i in range(rows):  
        for j in range(columns - 1): 
            for k in range(j + 1, columns):  
  
                if (matrix[i][j] == 1 and
                    matrix[i][k] == 1): 

                    if (j in table and k in table[j]): 
                        return True
  
                    if (k in table and j in table[k]): 
                        return True

                    if j not in table: 
                        table[j] = set() 
                    if k not in table: 
                        table[k] = set() 
                    table[j].add(k)  
                    table[k].add(j) 
    return False

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		r = int(input())
		c = int(input())
		line = input().strip().split()
		mat = [ [0 for _ in range(c)] for _ in range(r) ]
		for i in range(r):
			for j in range(c):
				mat[i][j] = int( line[i*c+j] )
		if (ValidCorner(mat)): 
			print("Yes") 
		else: 
			print("No") 
