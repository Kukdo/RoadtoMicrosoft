// 1.两数之和 遍历方法解决 时间复杂度较高
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Output = [] 
        for i in range(len(nums)):
            req = target - nums[i] # 作差获得需要找的第二个数
            for j in range(i+1, len(nums)): # 遍历查找需要找的第二个数在不在之后的区间中
                if req == nums[j]:
                    Output.append(i)
                    Output.append(j)
                    return Output
