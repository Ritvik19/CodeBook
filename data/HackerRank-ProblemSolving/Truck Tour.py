#!/bin/python3

import os
import sys


def truckTour(petrolpumps):
    start = 0
    passed = 0
    gas_in_tank = 0
    n = len(petrolpumps)
    while passed < n:
        pump = petrolpumps.pop(0)
        gas_in_tank += pump[0]
        if gas_in_tank >= pump[1]:
            passed += 1
            gas_in_tank -= pump[1]
        else:
            start += passed + 1
            passed = 0
            gas_in_tank = 0
        petrolpumps.append(pump)
    return start


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
