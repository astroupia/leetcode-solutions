str1 = "abcd"
str2 = "pq"

def mergeAlternately(word1, word2):
    left = 0
    right = 0
    newStr = ""
    while left < len(word1) and right < len(word2):
        if left <= right:
            newStr += word1[left]
            left += 1
        else:
            newStr += word2[right]
            right += 1
    
    while left < len(word1):
        newStr += word1[left]
        left += 1
    while right < len(word2):
        newStr += word2[right]
        right += 1

    return newStr

print(mergeAlternately(str1, str2))
        
