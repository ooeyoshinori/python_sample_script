#!/usr/local/bin/python3

import sys
import os
import argparse

def per(n):

    #import ipdb;ipdb.set_trace()

    if len(str(n))==1:
        print(n)
        print('DONE')
        return
    digits = [int(i) for i in str(n)] 
    result = 1 
    for j in digits: 
        result *= j 
    print(result)
    per(result)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-number',
                    required=True,
                    action='store',
                    help='please input number')

    args = parser.parse_args()
    per(args.number)

if __name__ == '__main__':
    main()
