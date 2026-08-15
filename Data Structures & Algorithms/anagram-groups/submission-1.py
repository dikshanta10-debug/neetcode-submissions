class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} #create dictionary
        
        for i in strs: #itereating through every word
            key = ''.join(sorted(i)) 
    #sorted i turned every word into a list in a sorted order
    #joins the individual letters into a new string


            if key not in groups:
                groups[key] = []
            #start off with key and empty
            
            groups[key].append(i)
            #we add the original word into that bin
        return list(groups.values())
        #return the list

       
        

            