count = 0
chef=["ch","che","chef","he","hef","ef"]
for n in range(int(input())):
    u = input()
    for c in chef:
        if c in u:
            count += 1
            break
            
print(count)