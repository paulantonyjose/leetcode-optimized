# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if t == "":
#             return ""

#         countT, window = {}, {}
#         for c in t:
#             countT[c] = 1 + countT.get(c, 0)

#         have, need = 0, len(countT)
#         res, resLen = [-1, -1], float("infinity")
#         l = 0
#         for r in range(len(s)):
#             c = s[r]
#             window[c] = 1 + window.get(c, 0)

#             if c in countT and window[c] == countT[c]:
#                 have += 1

#             while have == need:
#                 if (r - l + 1) < resLen:
#                     res = [l, r]
#                     resLen = r - l + 1
                    
#                 window[s[l]] -= 1
#                 if s[l] in countT and window[s[l]] < countT[s[l]]:
#                     have -= 1
#                 l += 1
#         l, r = res
#         return s[l : r + 1] if resLen != float("infinity") else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        c={}
        for character in t:
            c[character]=c.get(character,0) +1
        sliding_window={}
        have,need=0,len(c)
        result, length = [],float("infinity")

        for right in range(len(s)):
           #Avoids unecessary compute if string character is not in the substring
            if s[right] in t:
                sliding_window[s[right]] = sliding_window.get(s[right],0)+1
                if sliding_window[s[right]]==c[s[right]]:
                    have+=1
                while  have==need:
                    if right-left+1<length:
                        result=[left,right]
                        length = right-left+1
                    #conditions to avoid multiple statements only if character in main string exists in the sliding window variable
                    if s[left] in sliding_window:
                        sliding_window[s[left]]-=1
                        if  sliding_window[s[left]]<c[s[left]]:
                            have-=1
                    #changed position of left pointer to keep on incrementing and moving to right regardless of whether character exists in sliding window or not
                    left+=1 
        if result:
            left,right = result
        return s[left:right+1] if length!=float("infinity") else ''
