''''
@Time:2022/5/5 11:24       
@Author:OliverCHen
@Project: Algorithm   
@Description: 乘积小于 K 的子数组
'''
"""
给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
示例 1：

输入：nums = [10,5,2,6], k = 100
输出：8
解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-product-less-than-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 
"""
from typing import List

def numSubarrayProductLessThanK( nums: List[int], k: int) -> int:
    res, prio, i = 0, 1, 0
    for j, num in enumerate(nums):
        prio *= num
        while i <= j and prio >= k:
            prio //= nums[i]
            i += 1
        res += j-i+1
    return res

if __name__ == '__main__':
    ans = numSubarrayProductLessThanK([10,5,2,6],100)
    print(ans)



