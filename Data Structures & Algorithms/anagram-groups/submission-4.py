class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            s_sort = tuple(sorted(s))
            if s_sort in anagram_map:
                anagram_map[s_sort].append(s)
            else:
                anagram_map[s_sort] = [s]
        
        return list(anagram_map.values())