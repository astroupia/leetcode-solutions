s = "IceCreAm"

def reverseVowels(s):
        letters = list(s)
        left, right = 0, len(letters) - 1

        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u",]

        while left < right:
            while left < right and letters[left] in vowels:
                left += 1
            while left < right and letters[right] in vowels:
                right -= 1
            if left < right:
                letters[left], letters [right] = letters[right], letters[left]
                left += 1
                right -= 1

        return "".join(letters)

print(reverseVowels(s))