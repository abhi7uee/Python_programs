#TC: O(nlog(n)) | SC: O()
def nonConstructibleChange(coins):
    coins.sort()
    if coins[0] >1:
        return 1
    CurrentMaxChange = 0
    for element in coins:
        if element > CurrentMaxChange +1:
            return (CurrentMaxChange +1)
        elif element <= (CurrentMaxChange + 1):
            CurrentMaxChange = element + CurrentMaxChange
    return (CurrentMaxChange +1) #for array with consecutive nos.
            
coins =[5,7,1,1,2,3,22]
#coins = [1,2,3,4]
NC_sum = nonConstructibleChange(coins)
print(NC_sum)
