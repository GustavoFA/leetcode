from typing import List
from collections import Counter

"""
    Given an integer array nums and an integer k, return the k most frequent 
    elements within the array.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Approach 1: Using Counter + most_common() 

        Time Complexity:
        - O(n) to build the frequency map
        - O(n log k) to extract the k most frequent elements (heap of size k)
        Overall: O(n log k)

        Space Complexity:
        - O(n) for the frequency map

        where n = size of the input
        """
        return [item for item, _ in Counter(nums).most_common(k)]

    def topKFrequent_bucket(self, nums: List[int], k: int) -> List[int]:
        """
        Approach 2: Bucket Sort

        Time Complexity:
        - O(n) to build frequency map
        - O(n) to distribute elements into buckets
        - O(n) to scan buckets in reverse
        Overall: O(n)

        Space Complexity:
        - O(n) for frequency map
        - O(n) for buckets
        """
        counter = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counter.items():
            buckets[freq].append(num)
        
        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result     

if __name__ == "__main__":

    print(Solution().topKFrequent([1, 2, 3, 4, 4, 5, 6, 2, 4, 1, 8, 0], 3))
