class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def get_shortest_str(strs):
            shortest = strs[0]
            for i in range(1, len(strs)):
                if len(strs[i]) < len(shortest):
                    shortest = strs[i]
            return shortest
        
        prefix = ''
        if len(strs) == 0:
            return prefix
        shortest_str = get_shortest_str(strs)
        
        for i in range(len(shortest_str)):
            char = shortest_str[i]
            for j, el in enumerate(strs):
                if el[i] != char:
                    return prefix
            prefix += char
        return prefix
                
        
