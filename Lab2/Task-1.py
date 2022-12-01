class solution:
  def twoSum(self, nums, target):
       lookup = {}
       for i, num in enumerate(nums):
           if target - num in lookup:
               return (lookup[target - num], i )
           lookup[num] = i
print("index1=%d, index2=%d" % solution().twoSum((1,2,3,4,5,6,7,8,9,10,22,16,34,97,44,30),int(input("Enter a number: "))))
