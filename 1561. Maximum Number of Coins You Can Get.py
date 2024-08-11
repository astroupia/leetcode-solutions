class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        count = 0
        piles.sort(reverse = True)
        n = len(piles) - (len(piles) // 3)
        for i in range(0, len(piles[:n]), 2):
            count += piles[i+1]
        return count