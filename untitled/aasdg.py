from math import sqrt
nums=[0,2,3,4,5,6]
square=[i**2 for i in nums]
print(square)

nums = {int(sqrt(x)) for x in range(30)}
print(nums)