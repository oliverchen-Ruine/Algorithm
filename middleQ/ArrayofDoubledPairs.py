# -*- coding:utf-8 -*-
#@Time : 2022/4/1 12:07
#@Author: oliverchen
#@File : ArrayofDoubledPairs.py
#@Describe:二倍数对数组
'''
给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后
满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，
返回 true；否则，返回 false

输入：arr = [4,-2,2,-4]
输出：true
解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/array-of-doubled-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        '''
        本质上是问 arr能否分成 n/2对元素，其中每对元素中一个数是另一个数的两倍
        :param arr: 输入数组
        :return: 是否满足条件
        '''
        cnt = Counter(arr)#哈希计数器，key为List中值，value为该值的个数
        if cnt[0] % 2:
            return False
        print(sorted(cnt,key=abs))
        for x in sorted(cnt,key=abs):#按绝对值方式排序，sorted第一个参数为可迭代对象，key指明迭代对象
            if cnt[2 * x] < cnt[x]:
                return False
            cnt[2 * x] -= cnt[x]
        return True

if __name__ == '__main__':
    print(Solution.canReorderDoubled(Solution,[-2,-4,1,2]))


