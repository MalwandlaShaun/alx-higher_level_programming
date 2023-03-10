#!/usr/bin/python3

import calculator_1 as calculator

if __name__ == '__main__':

    a = 10
    b = 5

    result_1 = calculator.add(a,b)
    result_2 = calculator.sub(a,b)
    result_3 = calculator.mul(a,b)
    result_4 = calculator.div(a,b)

    print("{} + {} = {}".format(a,b,result_1))
    print("{} - {} = {}".format(a,b,result_2))
    print("{} * {} = {}".format(a,b,result_3))
    print("{} / {} = {}".format(a,b,result_4))
