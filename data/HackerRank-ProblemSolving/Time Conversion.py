import os
import sys

def timeConversion(s):
    hr, mn, sc = s.split(':')
    if sc[2:] == 'PM':
        hr = int(hr)+12 if hr != '12' else '12'
    else:
        hr = hr if hr != '12' else '00'
    sc = sc[:2]
    return ':'.join([str(hr), mn, sc])


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
