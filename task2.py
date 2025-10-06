#create a function to calculate variance of the given list.

# var = (xi - mu)**2 / no. of elem

nums = [2,3,4,5,6,7,1,3,4,5]

def variance(num: list):
    n = len(num)
    mean = sum(num)/n
    num = sum((x - mean)**2 for x in num)
    return num/n

print(variance(nums))