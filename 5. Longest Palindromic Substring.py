def longestPalindrome(s):
        def traverse(l, r):
            while l >= 0  and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1: r] 
        
        res = ""

        for i in range(len(s)):
            l, r = i, i 
            temp = traverse(l, r)
            if len(temp) > len(res):
                res = temp
            
            #when it's even
            temp = traverse(i, i+1)
            if len(temp) > len(res):
                res = temp
        return res