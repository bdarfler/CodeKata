'''
Created on May 15, 2009

@author: ben
'''

import re, sys

def smallestTempSpread(file_path = 'weather.dat', pattern=r'\s+(\d+)\D+(\d+)\D+(\d+)'):
    regex = re.compile(pattern)
    min = sys.maxsize
    with open(file_path) as f:
        for line in f:
            match = regex.match(line)
            if match:
                spread = int(match.group(2)) - int(match.group(3))
                if spread < min:
                    min = spread
                    ret = match.group(1)
    return ret

def smallestScoreSpread(file_path = 'football.dat', pattern=r'\s+\d+\.\s+([a-zA-Z_]+)(?:\D+\d+){4}\D+(\d+)\D+(\d+)'):
    regex = re.compile(pattern)
    min = sys.maxsize
    with open(file_path) as f:
        for line in f:
            match = regex.match(line)
            if match:
                spread = abs(int(match.group(2)) - int(match.group(3)))
                if spread < min:
                    min = spread
                    ret = match.group(1)
    return ret

def smallest(file_path, pattern):
    regex = re.compile(pattern)
    min = sys.maxsize
    with open(file_path) as f:
        for line in f:
            match = regex.match(line)
            if match:
                spread = abs(int(match.group(2)) - int(match.group(3)))
                if spread < min:
                    min = spread
                    ret = match.group(1)
    return ret

def smallestTempRefactor():
    return smallest(file_path = 'weather.dat', pattern=r'\s+(\d+)\D+(\d+)\D+(\d+)')


def smallestScoreRefactor():
    return smallest(file_path = 'football.dat', pattern=r'\s+\d+\.\s+([a-zA-Z_]+)(?:\D+\d+){4}\D+(\d+)\D+(\d+)')

if __name__ == '__main__':
    pass