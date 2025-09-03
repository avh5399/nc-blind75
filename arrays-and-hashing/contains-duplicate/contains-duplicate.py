class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        dupe = set()
        for num in nums:
            if num in dupe:
                return True
            dupe.add(num)
        return False




