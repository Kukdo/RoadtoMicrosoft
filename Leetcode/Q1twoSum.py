class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Output = []
        for i in range(len(nums)):
            req = target - nums[i]
            for j in range(i+1, len(nums)):
                if req == nums[j]:
                    Output.append(i)
                    Output.append(j)
                    return Output
