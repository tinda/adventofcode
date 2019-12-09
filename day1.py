#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main(argv):
    f = open("day1_input.txt", "r", encoding="utf-8")
    content = f.readlines()

    count = 0
    for content_number in content:
        answer = int(int(content_number) / 3) - 2
        print(answer)
        count = count + answer

    print(count)


if __name__ == '__main__':
    main(sys.argv)
