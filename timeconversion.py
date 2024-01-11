

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s:str) -> str:
    hours, minutes, seconds = s.split(':')    
    if s[-2:] == 'PM' and hours != '12':
        hours = str(int(hours) + 12)
    elif s[-2:] == 'AM' and hours == '12':
        hours = '00'
    return ':'.join([hours, minutes, seconds[:-2]])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
