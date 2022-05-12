# -*- coding:utf-8 -*-
#@Time : 2022/4/5 12:37
#@Author: oliverchen
#@File : CountPrimes.py
#@Describe:计数质数
class Solution:
    """
    给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。

    示例 1：
    输入：n = 10
    输出：4
    解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/count-primes
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def countPrimes(self, n: int) -> int:
        """
        埃氏筛，将质数x的倍数全部标记为合数
        :param n:
        :return:
        """
        isPrime = [1] * n
        ans = 0
        for i in range(2,n):
            if isPrime[i] == 1:
                ans += 1
                if i * i < n:
                    for j in range(i*i,n,i):
                        isPrime[j]=0
        return ans

