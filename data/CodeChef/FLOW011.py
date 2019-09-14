def floating_decimals(f_val, dec):
    prc = "{:."+str(dec)+"f}" #first cast decimal as str
    #print(prc) #str format output is {:.3f}
    return prc.format(f_val)

for i in range(int(input())):
    sal = int(input())
    if sal < 1500:
        gross = 2*sal
    else:
        gross = sal*198/100 + 500
    print(floating_decimals(gross,2))
