for t in range(int(input())):
    H, M = map(int, input().split())
    h_09 = min(10, H)
    h_11 = (H-1)//11
    m_09 = min(10, M)
    m_11 = (M-1)//11
    ans = min(h_09, m_09) + min(h_09-1, m_11) + min(h_11, m_09-1) + min(h_11, m_11)
    print(ans)
