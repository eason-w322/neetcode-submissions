class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        groups = defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(str))
            groups[sorted_str].append(str)
        
        for key in groups:
            results.append(groups[key])
        
        return results
            
            


