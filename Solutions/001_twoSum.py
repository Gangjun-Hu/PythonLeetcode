from typing import List

class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:  #类型注解
        numDict = dict() #创建一个字典
        for i in range(len(nums)):
            if target-nums[i] in numDict:
                return numDict[target-nums[i]], i
            numDict[nums[i]] = i
        return [0]

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    res = solution.twoSum(nums, target)
    print(res)
