nums=[1,6,4,2,2,3]
n=len(nums)

for i in range(n):
    while(nums[i]!=i+1 and nums[nums[i]-1]!=nums[i]):
        nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]

for i in range(n):
    print(nums[i])
