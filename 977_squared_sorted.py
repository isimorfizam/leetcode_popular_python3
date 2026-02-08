class Solution:
    # def sortedSquares0(self, nums: List[int]) -> List[int]:
    #     '''Time complexity : O(N) for loop + O(NlogN) for sort
    #     sort is the bottleneck if we want O(N)'''
    #     squared = []
    #     for num in nums :
    #         squared.append(num**2)
    #     squared.sort()
    #     return squared
        
    def sortedSquares1(self, nums: List[int]) -> List[int]:
        '''Split and merge : split to negative and positive'''

        def merge(pos,neg) :
            i = j = 0
            result = []

            while i < len(pos) and j < len(neg) :
                if pos[i]<neg[j] :
                    result.append(pos[i]**2)
                    i = i + 1 
                else :
                    result.append(neg[j]**2)
                    j = j + 1
            
            # add leftovers - if any
            if i<len(pos):
                [result.append(x**2) for x in pos[i:]]
            if j<len(neg):
                [result.append(x**2) for x in neg[j:]]

            return result
        

        # egde case
        if nums[0]>0 :
            return [num**2 for num in nums]

        # find first non-negative number
        # O(N)
        m = 0
        for ind, num in enumerate(nums):
            if num>=0:
                m = ind
                break

        # split into non-negative and negative part
        pos = nums[m:]
        # reverse negatives for sorting
        neg = [-1*num for num in reversed(nums[0:m])]

        # O(N)
        result = merge(pos, neg)

        
        return result

    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''Absolute and merge with deque + 2 pointers'''

        answer = collections.deque()
        left_pointer = 0 
        right_pointer = len(nums) - 1 # it looks from 2 directions

        while left_pointer<=right_pointer :
            left_value = abs(nums[left_pointer])
            right_value = abs(nums[right_pointer])
            if left_value>right_value:
                left_pointer +=1
                answer.appendleft(left_value**2)
            else :
                right_pointer -= 1
                answer.appendleft(right_value**2)

        return list(answer)
