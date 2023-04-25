class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}

        for word in strs:
            sortedword= "".join(sorted(list(word)))

            if sortedword not in dic:
                dic[sortedword]=[word]
            else:
                dic[sortedword].append(word)
        
        return  dic.values()