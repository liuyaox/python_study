#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 00:03:58 2019
@author: liuyao8
"""

import argparse

parser = argparse.ArgumentParser(description='Argparse Test.')  # description用于-h/--help输出内容的第一行

parser.add_argument(    # Positional Arguments   用【参数先后位置】来区分各参数
    'integers',         # Name of arguments
    metavar='N',
    type=int,
    
    # nargs: Number of arguments  
    #   N: N个参数-->list
    #   ?: 1个参数，若无参数，则使用default
    #   *: 所有参数-->list
    #   +: 同 '*'
    #   argparse.REMAINDER: 所有剩余参数-->list
    nargs='+',
    
    help='An integer for the accumulator'
)

parser.add_argument(    # Optional Arguments   用【前缀-或--】来区分各参数
    '-s'
    '--sum',            # List of option strings, e.g. foo or -f, --foo
    dest='accumulate',  # Name of argument，默认是上面list中第1个--前缀，若无--前缀，则第1个-前缀
    
    # action: 设置参数store的值
    #   store: default, 保存-s或--sum后跟随的值
    #   store_const: 保存const所指定的固定的值
    #   store_true/store_false: 保存True或False
    action='store_const',
    const=sum,          # 适用于action='store_const' or 'append_const'以及1个optional参数
    
    default=max,        # 命令行参数中，若无-s或--sum，则默认accumulate=max，否则使用设置的action与const，accumulate=sum
    help='sum the integers (default: find the max)'
)

args = parser.parse_args()
print(args.accumulate(args.integers))

# 文件用法
# python prog.py 1 2 3 4
# 返回4  因为命令行中无--sum或-s，则accumulate默认是max
# python prog.py 1 2 3 4 --sum
# 返回10 因为命令行中有--sum，则accumulate为action和const共同设置的sum


parser.add_argument(
    '-v',
    '--verbosity', 
    type=int,                           # 参数类型，默认str
    action='store_true',                # store_true表示不需要为-v指定参数值，其参数值就是True
    default=1,                          # 参数默认值
    help='Increase output verbosity'
) 

args = parser.parse_args()
print(args.echo)
