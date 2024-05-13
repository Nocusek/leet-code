class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last: int | None = None
        new: list[int] = []
        for n in nums:
            if last != n:
                new.append(n)
            last = n
        nums[:] = new

        return len(new)