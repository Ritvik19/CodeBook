def floating_decimals(f_val, dec):
    prc = "{:."+str(dec)+"f}" #first cast decimal as str
    #print(prc) #str format output is {:.3f}
    return prc.format(f_val)
for i in range(int(input())):
    inp = input().split(" ")
    q = int(inp[0])
    p = int(inp[1])
    if q > 1000:
        total = 0.9*q*p
    else:
        total = q*p
    print(floating_decimals(total,6))
