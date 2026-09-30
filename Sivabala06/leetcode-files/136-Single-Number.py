class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # grp={}
        # for i in nums:
        #     if i not in grp:
        #         grp[i]=0
        #     grp[i]+=1
        # k=list(grp.keys())
        # v=list(grp.values())
        # return k[v.index(1)]
        h=list(set(nums))
        dp=[0]*len(h)
        for i in nums:
            if i in h:
                dp[h.index(i)]+=1
        return h[dp.index(1)]


        