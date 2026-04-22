class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        wow_a_set = set()

        for n in nums:
            if n in wow_a_set:
                return True
            wow_a_set.add(n)
        return False