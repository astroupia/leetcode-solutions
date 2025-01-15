def reverseWords(s):
        new_str = s.split()
        reverse = new_str[::-1]
        return " ".join(reverse)

