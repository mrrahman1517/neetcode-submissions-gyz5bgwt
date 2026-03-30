class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [1] * len(nums)
        product = 1
        for num in nums:
            product *= num
            prefix.append(product)
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = product
            product *= nums[i]

        res = [0] * len(nums)
        for i in range(len(nums)):
            pre = prefix[i-1] if i > 0 else 1
            post = postfix[i]
            res[i] = pre * post
        return res
        