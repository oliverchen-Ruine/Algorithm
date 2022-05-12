# -*- coding:utf-8 -*-
#@Time : 2022/4/4 12:29
#@Author: oliverchen
#@File : RangeSumQueryMutable.py
#@Describe:区域和检索 - 数组可修改
"""
给你一个数组 nums ，请你完成两类查询。

    其中一类查询要求 更新 数组 nums 下标对应的值
    另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right

实现 NumArray 类：

    NumArray(int[] nums) 用整数数组 nums 初始化对象
    void update(int index, int val) 将 nums[index] 的值 更新 为 val
    int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和
    （即，nums[left] + nums[left + 1], ..., nums[right]）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-mutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class NumArray:
    """
    树状数组：可以动态维护序列前缀和的数据结构
    """
    def __init__(self, nums: List[int]):
        """
        构造树状数组,树状数组起点为1
        :param nums:
        :return:
        """
        self.nums = nums
        self.tree = [0] * (len(nums)+1)#格式化赋值全为0的数组，数组长度为nums长度+1，
        #从nums数组的1位置开始构造树状数组
        for i,num in enumerate(nums,1):
            self.add(i,num)

    def add(self,index:int,value:int):
        """
        单点修改:将第index个数增加value
        :param index: 修改位
        :param value: 修改值
        :return:
        """
        while index < len(self.tree):#小于
            #第index个数+value
            self.tree[index] += value
            #通过lowbit运算将更新到父结点
            index += index & -index

    def prefixSum(self,index:int) -> int :
        """
        求前缀和
        :param index: 前缀终点
        :return:
        """
        s = 0
        while index:
            #当前树结点所有左兄弟结点求和
            s += self.tree[index]
            #更新到左兄弟结点
            index -= index & -index
        return s

    def update(self, index: int, value: int) -> None:
        """
        更新nums数组和tree数组中index值
        :param index: nums中当前位
        :param value: 更新值
        :return:
        """
        #单点修改树状数组，tree数组是从1开始的，增加的分量为value - nums[index]
        self.add(index+1,value - self.nums[index])
        self.nums[index] = value#更新当前结点

    def sumRange(self, left: int, right: int) -> int:
        """
        区间求和，利用前缀和之差
        :param left: 区间起点
        :param right: 区间终点
        :return: 区间和
        """
        return self.prefixSum(right+1)-self.prefixSum(left)