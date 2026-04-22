class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            attempt = numbers[l] + numbers[r]
            if attempt == target:
                return [l+1, r+1]
            elif attempt < target:
                l += 1
            else:
                r -= 1
        
            