def kidsWithCandies(candies, extraCandies):
    max_val = max(candies)
    return [c + extraCandies >= max_val for c in candies]
