import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    db = []
    GMAIL = re.compile('.+@gmail\.com')
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if GMAIL.match(emailID):
            db.append(firstName)
    db.sort()
    for name in db:
        print(name)
