class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        hashmap = {}
        group = {}

        for i, val in enumerate(strs):
            key = ''.join(sorted(val))
            if key not in hashmap:
                hashmap[key] = i
            grouped_key = hashmap[key]
            if grouped_key not in group:
                group[grouped_key] = []
            group[grouped_key].append(val)
        
        return list(group.values())