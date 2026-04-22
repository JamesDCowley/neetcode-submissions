class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = []
        for n in nums:
            if n in lst:
                return True
            else:
                lst.append(n)
        return False