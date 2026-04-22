class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sequence = 0

        for n in nums:
            this_sequence = 0
            if not n-1 in nums_set:
                while n in nums_set:
                    this_sequence += 1
                    if this_sequence > sequence:
                        sequence = this_sequence
                    n += 1
        return sequence




                