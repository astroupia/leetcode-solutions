def palindromePermutation(s):
    if len(s) <= 1:
        return True
    freq = {}
    
    
    for right in range(len(s)):
        if s[right] in freq:
            del freq[s[right]]
        else:
            freq[s[right]] = freq.get(s[right], 0) + 1
        
            
    if len(freq) <= 1: 
        return True
    else:
        return False