# -*- coding:utf-8 -*-
#@Time : 2022/4/5 12:08
#@Author: oliverchen
#@File : PrimeNumber1.py
#@Describe:二进制表示中质数个计算置位

class Solution:
    """
    给你两个整数 left 和 right ，在闭区间 [left, right] 范围内，统计并返回 计算置位位数为质数 的整数个数。

    计算置位位数 就是二进制表示中 1 的个数。

    例如， 21 的二进制表示 10101 有 3 个计算置位

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        :param left: 区间起点
        :param right: 区间终点
        :return:
        """
        return sum(self.isPrime(self.count1(x)) for x in range(left,right+1))

    def isPrime(self,x: int) -> bool:
        """
        暴力枚举 2到根号x
        :param x:
        :return:
        """
        if x < 2:
            return False
        i = 2
        while i * i <= x:
            if x % i ==0:
                return False
            i +=1
        return True

    def count1(self,value : int ) -> int:
        """
        统计二进制数中1的个数
        :param value: 二进制数
        :return:
        """
        ans = 0
        i = value
        while i!=0:
            #移除最低位
            i -= self.lowbit(i)
            ans +=1
        return ans

    def lowbit(self,value : int) -> int:
        """
        lowbit运算
        :param value:
        :return:
        """
        return value & (-value)

