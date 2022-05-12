# -*- coding:utf-8 -*-
#@Time : 2022/3/30 12:18
#@Author: oliverchen
#@File : TwoSum.py
#@Describe: 给定一个整数数组 nums 和一个整数目标值 target，
#           请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标

#导入限定方法参数类型
from typing import List
class TwoSum:
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        hash_table = dict()#哈希表
        for i,value in enumerate(nums):
            a = target - value
            if a in hash_table:
                return [hash_table[a],i]
            hash_table[nums[i]]=i
        return []

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    L = TwoSum.twoSum(TwoSum,nums,target)
    print(L)