def kLengthString(s, k):
    left, result = 0, 0
    freq = {}
    
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        
        while freq[s[right]] > 1 or (right - left + 1) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        
        if (right - left + 1) == k:
            result += 1
        
    return result