def TowerOfHanoi(n , beg, end, aux): 
    if n == 1: 
        print(f"Move disk 1 from rod {beg} to rod {end}")
        return
    TowerOfHanoi(n-1, beg, aux, end) 
    print(f"Move disk 1 from rod {beg} to rod {end}")
    TowerOfHanoi(n-1, aux, end, beg) 


if __name__ == "__main__":
    TowerOfHanoi(4, 'A', 'C', 'B')