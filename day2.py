#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main(argv):
    txt = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,1,47,6,51,1,13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,1,95,10,99,1,9,99,103,2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,127,1,127,9,0,99,2,0,14,0"

    # txt = "1,9,10,3,2,3,11,0,99,30,40,50"
    # txt = "1,1,1,4,99,5,6,0,99"

    x = txt.split(",")

    for i in range(0, len(x), 4):
        # print(str(i) + "->" + str(x[i]))
        if(x[i] == '1'):
            x[int(x[int(i)+3])] = str(int(x[int(x[int(i)+1])]) +
                                      int(x[int(x[int(i)+2])]))
        elif(x[i] == '2'):
            x[int(x[int(i)+3])] = str(int(x[int(x[int(i)+1])]) *
                                      int(x[int(x[int(i)+2])]))
        elif(x[i] == '99'):
            continue
    print(x)

    # other code

    myfile = open("day2_input.txt", "r").read().split(",")

    for i in range(len(myfile)):
        myfile[i] = int(myfile[i])

    myfile[1] = 12
    myfile[2] = 2

    for i in range(len(myfile)):
        if i % 4 == 0:
            opcode = myfile[i]
            operand1 = myfile[i+1]
            operand2 = myfile[i+2]
            register = myfile[i+3]
            print("Instr:", opcode, operand1, operand2, register)
            if myfile[i] == 99:
                print("Breaking...")
                break
            if opcode == 1:
                myfile[register] = operand1 + operand2
                print("Register", register, "stored", myfile[register])
            elif opcode == 2:
                myfile[register] = operand1 * operand2


if __name__ == '__main__':
    main(sys.argv)
