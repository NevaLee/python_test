# -*- coding: utf-8 -*-
# @Time : 2021/8/10 20:48
# @Author : Lihq
# @File : rabbit_test.py
# @Software: PyCharm
import collections


cell_list = [[0,0,0,1],[1,0,0,0,],[0,0,0,0]]  # 兔子回家的路，”1“代表蛇，”0“代表无蛇
M,N = len(cell_list),len(cell_list[0])  #



def problem_1_question_A(cell_list,M,N):
    """
    求兔子回家在途中不遇到蛇，一共右多少条路
    时间复杂度为  O(M * N)
    空间复杂度为 O(M * N)
    :param cell_list: 兔子回家的cell
    :param M:
    :param N:
    :return: 兔子回家的路的数量
    """

    que = collections.deque()
    path_cnt = 0  # 兔子回家的路数
    que.appendleft([0,0])
    while que:
        x,y = que.pop()
        if x == M-1 and y == N -1:  # 兔子到家了
            path_cnt += 1
        if 0 <= x + 1 < M and cell_list[x + 1][y] != 1:  # 兔子没到家并且没遇到蛇
            que.appendleft([x+1,y])
        if 0 <= y + 1 < N and cell_list[x][y + 1] != 1:  # 兔子没到家并且没遇到蛇
            que.appendleft([x, y + 1])
    print(path_cnt)  # 打印兔子回家的路的数量
    return path_cnt


def problem_1_question_C(cell_list,M,N):
    """
    使用广度优先,输出兔子回家的路径
    :param cell_list:
    :param M:
    :param N:
    :return:
    """
    que = collections.deque()
    que.appendleft([[0,0]])
    all_path_list = list()
    # path_dict = dict()
    # path_dict["0_0"] = [[0, 0]]

    while que:
        path_list = que.pop()
        x,y = path_list[-1]
        right= 0
        if x == M-1 and y == N -1:  # 兔子到家了
            all_path_list.append(path_list)
            # print(path_list)
        if 0 <= x + 1 < M and cell_list[x + 1][y] != 1:  # 兔子没到家并且没遇到蛇
            # right_list = path_list[:]
            path_list.append([x+1,y])
            que.appendleft(path_list)
            right = 1
        if 0 <= y + 1 < N and cell_list[x][y + 1] != 1:  # 兔子没到家并且没遇到蛇
            down_list = path_list[:]
            down_list.append([x, y + 1])
            que.appendleft(down_list)
    return all_path_list


problem_1_question_A(cell_list,M,N)
problem_1_question_C(cell_list,M,N)