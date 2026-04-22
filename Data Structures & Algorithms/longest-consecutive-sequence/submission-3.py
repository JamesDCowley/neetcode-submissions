class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest_sequence = 0
        for n in nums:
            if n-1 not in nums_set:
                seq = 0
                i = n
                while i in nums_set:
                    seq += 1
                    i += 1
                longest_sequence = max(longest_sequence, seq)
        return longest_sequence
                