
def twoSum(nums,target):
    nums_map = {}
    for i in range(len(nums)):
        if nums_map.__contains__(target-nums[i]):
            return [nums_map.get(target-nums[i]),i]
        else:
            nums_map[nums[i]] = i


print(twoSum([2, 7, 11, 15], 9))

# Time Complexity: O(N)
# Only use for-loop one time, so it would be O(N)
