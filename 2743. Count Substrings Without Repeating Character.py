def findSubString(s):
    res, l = 0, 0
    freq = {}
    
    for r in range(len(s)):
        freq[s[r]] = freq.get(s[r], 0) + 1
        
        while freq[s[r]] > 1:
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l += 1
            
        res += r - l + 1
            
    return res
            