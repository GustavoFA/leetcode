from typing import List

class Solution:

    """
    Design an algorithm to encode a list of strings to a string. 
    The encoded string is then sent over the network and is decoded back to the original list of strings.
    """
    
    """
    Encoder -> O(n)
    Decoder -> O(n)
    """

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
                
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            words.append(word)
            
            i = j + length + 1 
        
        return words

if __name__ == "__main__":
    
    solution = Solution()
    
    msg = solution.encode(["Hello", "World"])
    print(f'Encode message: {msg}')
    print(f"Decode message: {solution.decode(msg)}")
    