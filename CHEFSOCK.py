jacketCost, sockCost, money = map(int, input().split())
if ((money - jacketCost) // sockCost) %2 == 1:
    print("Unlucky Chef")
else:
    print("Lucky Chef")
