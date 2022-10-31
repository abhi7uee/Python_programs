#Method 1: brute force algo
def threeNumberSort(array, order):
    count1 =0
    count2 =0
    count3 =0
    for element in array:
        if element == order[0]:
            count1 += 1
        elif element == order[1]:
            count2 += 1
        elif element == order[2]:
            count3 += 1

array =[1,0,0,-1,-1,0,1,1]
order = [0,1,-1]

output_array = threeNumberSort(array, order)
print(output_array)
