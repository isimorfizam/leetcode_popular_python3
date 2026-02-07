import numpy as np

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # edge case - half the target
        if target%2==0 :
            print('edge case - half the target')
            hlf_trgt = target//2
            result = np.where(np.array(nums)==hlf_trgt)[0] # returns indices 
            print(result)
            if isinstance(result, np.ndarray) and len(result)>1:
                return [int(result[0]), int(result[1])]
            elif len(result) == 1:  : # catches when hlf_trgt is in array, but only once and sets that index to target - so if we deduce target-target = 0 which is not an integer and will not be found in the original nums
                nums[result[0]] = target

        
    
        print('not an edge case, moving on')
        target_list = [target]*len(nums)
        result_array = np.array(target_list) - np.array(nums)
        print(f'input : {nums}')
        print(f'needed output for each input : {result_array}')
        result = list(set(nums).intersection(set(result_array))) # should be two values automatically if exists
        print(f'values that add up to target : {result}')
        return ([nums.index(result[0]), nums.index(result[1])])


    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # hash map principle
        nums_dict = {}
        
        for position in range(len(nums)) :
            print(f'Looking for match for number {num} at index {position}')
            expected_result = target - nums[position]
            if expected_result in nums_dict :
                print(f'Found for number {num} at position {position}')
                print(f'input : {nums}')
                return ([position, nums_dict[expected_result]])
            else : print('Not found yet')

            nums_dict[nums[position]] = position
            print(nums_dict)

'''
Time complexity : 
Edge-case numpy where O(n)
Create lists/array O(n)
Set operations O(n)
Two index searches O(n)


Space complexity:
	•	numpy arrays (multiple): O(n)
	•	target_list: O(n)
	•	result_array: O(n)
	•	sets: O(n)