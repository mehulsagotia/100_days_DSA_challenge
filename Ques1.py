
#Q1 Maximum and minimum of an array using minimum number of comparisons
def getMinMax(arr):
    arr.sort()
    minmax = {"min": arr[0], "max": arr[-1]}
    return minmax


arr = [10, 11, 445, 1, 330, 300]
minmax = getMinMax(arr)

print("Minimum element is", minmax["min"])
print("Maximum element is", minmax["max"])