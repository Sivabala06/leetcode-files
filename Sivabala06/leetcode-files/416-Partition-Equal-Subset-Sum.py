class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # i=len(nums)//2
        # if sum(nums)%2 !=0:
        #     return False
        # if len(nums)==1:
        #     return False

        # s1=nums[:i]
        # s2=nums[i:]
        # if sum(s1)==sum(s2):
        #     return True
        # while(len(s1)>1 and len(s2)>1):
        #     if sum(s1)<sum(s2):
        #         m=min(s2)
        #         s2.remove(m)
        #         s1.append(m)
        #     if sum(s1)>sum(s2):
        #         m=min(s1)
        #         s1.remove(m)
        #         s2.append(m)
        #     if sum(s1)==sum(s2):
        #         return True
                
        # return False
        tot=sum(nums)
        if tot%2 !=0:
            return False
        target=tot//2
        # reachable_sums = {0}

        # for num in nums:
        #     new_sums = set()
        #     for s in reachable_sums:
        #         candidate = s + num
        #         if candidate == tar:
        #             return True
        #         if candidate < tar:
        #             new_sums.add(candidate)
            
        #     # Combine the new sums with the old ones
        #     reachable_sums.update(new_sums)

        # return tar in reachable_sums
        dp = [False] * (target + 1)
        
        # Base case: sum 0 is always possible (pick no elements)
        dp[0] = True

        for num in nums:
            # Step backwards from target down to num
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
 



        