'''
Start
Backpack = []
↓
Take A
[A]
↓
Take B
[A, B]
↓
Finished exploring
Pop
[A]
↓
Finished exploring A
Pop
[]
'''
def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        results = []
        current = []
        def backtrack(index):
            if index == n:
                results.append(current[:]) # add copy of solution
                return
            # Don't pick
            backtrack(index+1)
            # Pick 
            current.append(nums[index])
            backtrack(index+1)
            current.pop()
        backtrack(0)
        return results