class pair_elements:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i

value = int(input("Enter sum for which you want to make this search: "))

number_range = tuple(range(0, 1001))

result = pair_elements().twoSum(number_range, value)
if result:
    print("index1=%d, index2=%d" % result)
else:
    print("No pair found.")
