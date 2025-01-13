# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:58:29 2025

@author: dell
"""

def fib_seq(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq





def main():
    print("__Fibonacci Sequence__")
    print(fib_seq(5))
    
    

if __name__ == "__main__":
    main()