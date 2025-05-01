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
        
        print(self._nums)
    
    def twoSum(self) -> List[int]:
        """

        """
        print('Two sum function option.')
        
        _indices = {}

        for i, n in enumerate(self._nums):
            _indices[n] = i
        
        for i, n in enumerate(self._nums):
            _diff = self._target - n
            if _diff in _indices and _indices[_diff] != i:
                return [i, _indices[_diff]]
    
    def twoSum_forced(self) -> List[int]:
        """
        
        """
        for i in range(len(self._nums)):
            for j in range(i+1, len(self._nums)):
                if i == j:
                    continue
                if self._nums[i] + self._nums[j] == self._target:
                    return [i, j]
    
if __name__ == "__main__":
    print('The code has been started!')
    _checker = TwoSum(nums=eval(input('Insert the array of integers:\n')), 
                        target=int(input('Insert the integer target:\n')))
    
    ret = _checker.twoSum_forced()
    
    print(ret)