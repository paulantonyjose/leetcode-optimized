'''class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a>0:
                break
            if i>0 and a==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                threesum = a +nums[l] +nums[r] 
                if threesum >0:
                    r-=1
                elif threesum<0:
                    l+=1        
                else:
                    if threesum == 0:
                        res.append([a,nums[l],nums[r]])
                        l+=1
                        r-=1
                        while nums[l] == nums[l-1] and l<r:
                            l+=1
                        while nums[r] == nums[r+1] and l<r: #Right pointer will be subtracted and moved to the left so that impossible condition =>  a + nums[l] + nums[r] ==0 isn't computed unnecassarily
                            r-=1


        return res
