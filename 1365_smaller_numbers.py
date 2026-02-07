class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        position_map = {}

        for i, num in enumerate(sorted_nums):
            if num not in position_map:
                position_map[num] = i

        return [position_map[num] for num in nums]
    