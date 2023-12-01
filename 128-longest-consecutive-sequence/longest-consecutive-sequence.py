class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = defaultdict(list) # keep track of length
        visited = set()
        longest = 0
        for v in nums:
            if v in visited:
                continue
            l, r = v, v
            if v+1 in m:
                r = m[v+1][1]
            if v-1 in m:
                l = m[v-1][0]
            m[l] = [l, r]
            m[r] = [l, r]
            longest = max(longest, r-l+1)
            visited.add(v)
        return longest
            
