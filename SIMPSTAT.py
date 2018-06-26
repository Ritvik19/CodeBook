def floating_decimals(f_val, dec):
    prc = "{:."+str(dec)+"f}" #first cast decimal as str
    #print(prc) #str format output is {:.3f}
    return prc.format(f_val)

for i in range(int(input())):
    inp = input().split(" ")
    n = int(inp[0])
    k = int(inp[1])
    A = [int(e) for e in input().split(" ")]
    sum = 0
    for a in sorted(A)[k: n-k]:
        sum += a
    print(floating_decimals(sum/(n-2*k), 6))
