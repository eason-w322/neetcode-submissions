class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        groups = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in groups:
                groups[sorted_str] = []
            groups[sorted_str].append(str)
        
        for key in groups:
            results.append(groups[key])
        
        return results
            
            


