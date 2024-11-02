#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019-06-03
@author: liuyao8
"""

from multiprocessing import Pool


def func1(x):
    return x + 1
    
def func2(x, y, z):
    return x + y + z

def main():
    thread_count = 4    # 进程个数
    pool = Pool(thread_count)

    # 并行运行单参数函数
    res1 = pool.map(func1, range(5))
    print(res1)         # [1, 2, 3, 4, 5]

    # 并行运行多参数函数
    res2 = pool.starmap(func2, zip([1, 2, 4], [2, 4, 8], [3, 6, 12]))
    pool.terminate()
    print(res2)         # [6, 12, 24]


# 注意！Functionality within multiprocessing requires that the __main__ module be importable by the children
if __name__ == '__main__':
    main()
