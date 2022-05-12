# -*- coding:utf-8 -*-
#@Time : 2022/3/31 12:10
#@Author: oliverchen
#@File : SelfDividingNumbers.py
#@Describe:自除数
"""
自除数 是指可以被它包含的每一位数整除的数。

    例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

自除数 不允许包含 0 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/self-dividing-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class SelfDividingNumbers:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """
        自除数判断方法
        :param self:懂得都懂
        :param left:区级左起点
        :param right:区间右起点
        :return:满足自除数性质的数
        """
        L = list()
        for i in range(left,right+1):
            value = i
            flag = True
            while i!=0:
                #divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
                i, a = divmod(i,10)
                if a == 0 or value % a != 0:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                L.append(value)
        return L

if __name__ == '__main__':
    print(SelfDividingNumbers.selfDividingNumbers(SelfDividingNumbers,1,22))


