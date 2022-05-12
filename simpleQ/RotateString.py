# -*- coding:utf-8 -*-
#@Time : 2022/4/7 15:16
#@Author: oliverchen
#@File : RotateString.py
#@Describe:旋转字符串

class Solution:
    """
    给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。
    s 的 旋转操作 就是将 s 最左边的字符移动到最右边。
    例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea' 。
    示例 1:

    输入: s = "abcde", goal = "cdeab"
    输出: true

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/rotate-string
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def rotateString(self, s: str, goal: str) -> bool:
        """
        查找比对，从待旋转字符串中第一个开始比对
        :param s: 待旋转字符串
        :param goal: 目标字符串
        :return:
        """
        m,n = len(s),len(goal)
        if m != n:
            return False
        L = []
        for i in range(n):
            if s[i] == goal[0]:
                L.append(i)
        for i in L:
            if self.isSame(i,s,goal,n):
                return True
        return False

    def isSame(self,i: int,s: str, goal: str,n: int) -> bool:
        """
        从旋转为i比对
        :param i: 旋转位
        :param s: 待旋转字符串
        :param goal: 目标字符串
        :param n: 字符串长
        :return:
        """
        for j in range(n):
            if s[(i+j) % n] != goal[j]:
                return False
        return True



