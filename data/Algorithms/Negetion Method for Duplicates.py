def checkDuplicatesNegationTechnique(A):
    for i in range(len(A)):
        if A[abs(A[i])] < 0:
            return True
        else:
            A[A[i]] = - A[A[i]]
    return False


if __name__ == "__main__":
    A = [3, 2, 1, 2, 2, 3]
    print(f"Duplicates Exist in A: {checkDuplicatesNegationTechnique(A)}")
    B = [0, 2, 1]
    print(f"Duplicates Exist in B: {checkDuplicatesNegationTechnique(B)}")
