class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angMap = {}
        for i in strs:
            strMap = [0] * 26
            for j in i:
                strMap[ord(j) - ord('a')] += 1
            strMap = tuple(strMap)
            if strMap in angMap:
                angMap[strMap].append(i)
            else:
                angMap[strMap] = [i]
        
        return [i for i in angMap.values()]
