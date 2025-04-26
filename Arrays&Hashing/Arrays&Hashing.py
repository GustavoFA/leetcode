from typing import List

class ArraysAndHashing:

     class hasDuplicated:
        """
            Given an integer array nums, return true if any value appears 
            more than once in the array, otherwise return false.
        """
        def __init__(self, nums: List[int]):
            self.nums = nums

        def sorting(self) -> bool:
            """
                Using sorting -> Time : O(nlogn) | Space : O(1)
            """
            self.nums.sort()
            return any(self.nums[i] == self.nums[i-1] for i in range(1, len(self.nums)))
        
        def hash_set(self) -> bool:
            """
                Using hash set -> Time : O(n) | Space : O(n)
            """
            numsHashSet = set()
            return any(num in numsHashSet or numsHashSet.add(num) for num in self.nums)

        def hash_set_length(self) -> bool:
            """
                Hash set length -> Time : O(n) | Space : O(n)
            """
            return len(set(self.nums.copy())) < len(self.nums)


if __name__ == "__main__":

    # checking solutions
    while True:
        _checker = ArraysAndHashing().hasDuplicated(nums=eval(input('Insert the list of int:\n')))
        print(f'Answer: {_checker.hash_set()}')
