# Create a list of numbers and find out the maximum number

num = [1,2,3,4,5,6,7,8,9,10,12,34,21,34,6]
num.sort()
maxx = num[0]
for i in num:
    for j in num:
        if i > j:
            maxx = i
print(maxx)


