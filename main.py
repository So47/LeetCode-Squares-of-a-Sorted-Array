class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            result.append(num**2)

        result.sort()  
        return result

        # return sorted(num**2 for num in nums)
