class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t) #sort 사용!
    
#         if len(s) != len(t):
#             return False
        
#         countS, countT = {}, {}
        
#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             #해쉬맵 #get으로 해쉬맵이 없으면 0으로 돌아옴
#             countS[t[i]] = 1 + countS.get(s[i], 0) #t로 변경
            
#         for c in countS:
#             if countS[c] != countT.get(c,0):
#                 return False
            
#         return True
                
            
            return sorted(s) == sorted(t)