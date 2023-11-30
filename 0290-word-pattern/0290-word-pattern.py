class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = dict()
        words = s.split()

        if len(words) != len(pattern):
            return False

        for i, p in enumerate(pattern):
            if p not in m:
                # values is a set - fast membership testing
                if words[i] not in m.values(): 
                    m[p] = words[i]
                else:
                    return False
            elif p in m and m[p] != words[i]: 
                return False
        return True