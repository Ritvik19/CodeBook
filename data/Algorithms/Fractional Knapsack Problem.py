class Item: 
    def __init__(self, wt, val, ind): 
        self.wt = wt 
        self.val = val 
        self.ind = ind 
        self.cost = val // wt 
  
    def __lt__(self, other): 
        return self.cost < other.cost 
  
# Greedy Approach 
def getMaxValue(wt, val, capacity): 
    iVal = [] 
    for i in range(len(wt)): 
        iVal.append(Item(wt[i], val[i], i)) 

    iVal.sort(reverse = True) 

    totalValue = 0
    for i in iVal: 
        curWt = int(i.wt) 
        curVal = int(i.val) 
        if capacity - curWt >= 0: 
            capacity -= curWt 
            totalValue += curVal 
        else: 
            fraction = capacity / curWt 
            totalValue += curVal * fraction 
            capacity = int(capacity - (curWt * fraction)) 
            break
    return totalValue 

if __name__ == "__main__": 
    wt = [10, 40, 20, 30] 
    val = [60, 40, 100, 120] 
    capacity = 50
    print("Maximum value in Knapsack =", getMaxValue(wt, val, capacity))