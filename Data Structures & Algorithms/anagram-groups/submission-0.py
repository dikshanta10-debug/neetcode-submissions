class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #initialize a dictionary
        for s in strs: #iterates through every string
            sortedS = ''.join(sorted(s)) #sorts the chars of the string in alphabical order and returns a list
            res[sortedS].append(s) #uses the sorted string as a key and apends s 
        return list(res.values()) #returns the groups


        