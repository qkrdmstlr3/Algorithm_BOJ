"""
    Author : ParkEunsik
    Date   : 2019/07/09
    url    : https://www.acmicpc.net/problem/10991
"""
N = int(input())

for i in range(1, N+1):
    print(' '*(N-i), '* '*i, sep='')
