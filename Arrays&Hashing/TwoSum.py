from typing import List

class TwoSum:
    """
        Given an array of integers nums and an integer target, 
        return the indices i and j such that 
        nums[i] + nums[j] == target and i != j.
    """
    
    def __init__(self, nums: List[int], target: int):
        self._nums = nums
        self._target = target

    def twoSumSorting(self) -> List[int]:
        """
            Sorting mode -> Time : O(nlogn) | Space : O(n)
        """
        mm = []
        for i, num in enumerate(self._nums):
            mm.append([num, i])

        mm.sort()
        i, j = 0, len(self._nums) - 1

        while i < j:
            _buffer = mm[i][0] + mm[j][0]
            if _buffer == self._target:
                return[min(mm[i][1], mm[j][1]),
                       max(mm[i][1], mm[j][1])]
            elif _buffer < self._target:
                i += 1
            else:
                j -= 1
    
    def twoSumHashMap(self) -> List[int]:
        """ 
            Hash map -> Time : O(n) | Space : O(n)
        """
        print('Two sum function using hash map')
        
        _indices = {}

        for i, n in enumerate(self._nums):
            _indices[n] = i
        
        for i, n in enumerate(self._nums):
            _diff = self._target - n
            if _diff in _indices and _indices[_diff] != i:
                return [i, _indices[_diff]]
            
    def twoSumHasMap_(self) -> List[int]:
        """
            Hash map (fewer steps) -> Time : O(n) | Space : O(n)
        """
        _map = {}

        for i, n in enumerate(self._nums):
            _diff = self._target - n
            if _diff in _map:
                return [_map[_diff], i]
            _map[n] = i
    
    def twoSum(self) -> List[int]:
        """
            Brute force -> Time : O(n²) | Space : O(1)
        """
        for i in range(len(self._nums)):
            for j in range(i+1, len(self._nums)):
                if self._nums[i] + self._nums[j] == self._target:
                    return [i, j]
    
if __name__ == "__main__":
    
    while True:
        _checker = TwoSum(nums=eval(input('Insert the array of integers:\n')), 
                            target=int(input('Insert the integer target:\n')))
        
        print(_checker.twoSumHasMap_())
    