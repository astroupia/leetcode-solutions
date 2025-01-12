def candieMax(candies, extraCandies):
    maxCandies = max(candies)
    result = [(candy + extraCandies) >= maxCandies for candy in candies]
    return result
