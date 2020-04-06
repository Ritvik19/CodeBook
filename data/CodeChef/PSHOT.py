for t in range(int(input())):
    N = int(input())
    shots = input()
    nums_A, nums_B, A_remaining, B_remaining = 0, 0, N, N
    ans = 2 * N
    curr = 1
    for i, v in enumerate(shots):
        if curr :
            A_remaining -= 1
            nums_A += int(v)
            curr = 1 - curr
        else:
            B_remaining -= 1
            nums_B += int(v)
            curr = 1 - curr
        if nums_A > (nums_B + B_remaining) or nums_B > (nums_A + A_remaining):
            ans = i + 1
            break
    print(ans)