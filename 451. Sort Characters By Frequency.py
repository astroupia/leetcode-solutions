class Solution:
    def frequencySort(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        countDict = {}
        for i in s:
            if countDict.get(i) is None:
                countDict[i] = 1 
            else:
                countDict[i] += 1

        sortedDict = sorted(countDict.items(), key=lambda item: item[1], reverse = True)

        freqList = []
        for char, freq in sortedDict:
            freqList.append(char * freq)
        
        return "".join(freqList)
        
