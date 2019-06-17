n = int(input())
a = [int(e) for e in input().split(" ")]
ce = 0
co = 0
for e in a:
    if e%2 == 0:
        ce += 1
    else:
        co += 1
if ce > co:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
