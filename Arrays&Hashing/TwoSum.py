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
    
    def twoSum(self) -> List[int]:
        """
            Brute force -> Time : O(n²) | Space : O(1)
        """
        for i in range(len(self._nums)):
            for j in range(i+1, len(self._nums)):
                if self._nums[i] + self._nums[j] == self._target:
                    return [i, j]
    
if __name__ == "__main__":
    print('The code has been started!')
    _checker = TwoSum(nums=eval(input('Insert the array of integers:\n')), 
                        target=int(input('Insert the integer target:\n')))
    
    ret = _checker.twoSum_forced()
    
    print(ret)