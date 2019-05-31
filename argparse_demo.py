#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 00:03:58 2019
@author: liuyao8
"""

import argparse

parser = argparse.ArgumentParser(description='Argparse Test.')
parser.add_argument(        # Positional Arguments   用【参数先后位置】来区分各参数
        'integers',
        metavar='N',
        type=int,
        
        # nargs: Number of arguments  
        #   N: N arguments present will be gathered into a list  
        #   ?: one argument if possible and produced as a single item. If no argument present, use default
        #   *: All arguments present will be gathered into a list
        #   +: 同 '*'
        #   argparse.REMAINDER: All the remaining arguments will be gathered into a list.
        nargs='+',
        
        help='An integer for the accumulator'
)
parser.add_argument(        # Optional Arguments   用【前缀-或--】来区分各参数
        '--sum',
        
        # dest: The name of the attribute to be added to the object returned by parse_args()
        dest='accumulate',
        
        # action: ArgumentParser objects associate arguments with actions
        #   store: default, just store argument's value
        #   store_const: store argument's value specified by the const keyword argument
        action='store_const',
        
        # const: Used to hold constant values that are not read from command line but are required for the various ArgumentParser actions
        #   When action='store_const' or 'append_const'
        #   When called with option strings (like -f or --foo) and nargs='?'
        const=sum,
        
        default=max,
        help='sum the integers (default: find the max)'        
)
args = parser.parse_args()
print(args.accumulate(args.integers))

# 文件用法
# python prog.py 1 2 3 4
# 返回4
# python prog.py 1 2 3 4 --sum
# 返回10


parser.add_argument(
        '-v',                               # 
        '--verbosity', 
        help='Increase output verbosity', 
        type=int,                           # 参数类型，默认str
        default=1,                          # 参数默认值
        action='store_true'                 # store_true表示不需要为-v指定参数值
) 

args = parser.parse_args()
print(args.echo)
