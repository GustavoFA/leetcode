from collections import Counter

class ValidAnagram:
    """
        Given two strings s and t, return true if the two strings are anagrams of each other,
        otherwise return false.
    """
    
    word_s = None
    word_t = None
    
    def __init__(self, s: str, t: str):
        self.word_s = s
        self.word_t = t
    
    def isAnagram_counter(self) -> bool:
        """
            Using Counter function from collections. This function count the number of each character of the
            string.
        """
        
        print('Using Counter function ...')
        
        if len(self.word_s) != len(self.word_t):
            return False
        
        return Counter(self.word_s) == Counter(self.word_t)

    def isAnagram_sorted(self) -> bool:
        """
            Using sort function.
            
            Time : O(nlogn + mlogm) | Space : O(1) or O(n+m)
        """
        print('Using sort function ...')
        
        if len(self.word_s) != len(self.word_t):
            return False
        
        return sorted(self.word_s) == sorted(self.word_t)
    
    def isAnagram_hash(self) -> bool:
        """
            Using hash maps (dicts).
            
            Time : O(n+m) | Space : O(1)
        """
        print('Using hash map ...')
        
        if len(self.word_s) != len(self.word_t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(self.word_s)):
            countS[self.word_s[i]] = 1 + countS.get(self.word_s[i], 0)
            countT[self.word_t[i]] = 1 + countT.get(self.word_t[i], 0)
        return countS == countT

    def isAnagram_array(self) -> bool:
        """
            Using hash with array.
        """
        print('Using Arrays to construct Hash table ...')
        
        if len(self.word_s) != len(self.word_t):
            return False
        
        _count = [0] * 26
        
        for i in range(len(self.word_s)):
            _count[ord(self.word_s[i]) - ord('a')] += 1
            _count[ord(self.word_t[i]) - ord('a')] -= 1
        
        for k in _count:
            if k != 0:
                return False
            
        return True

if __name__ == "__main__":
   
    while True:
        _checker = ValidAnagram(s=input('Insert one word:\n'), t=input('Insert another word:\n'))
        print(f'Answer: {_checker.isAnagram_sorted()}')