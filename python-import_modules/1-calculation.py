#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

a = 10
b = 5
resultadd = add(a, b)
print("{} + {} = {}".format(a, b, resultadd))

resultsub = sub(a, b)
print("{} - {} = {}".format(a, b, resultsub))

resultmul = mul(a, b)
print("{} * {} = {}".format(a, b, resultmul))

resultdiv = div(a, b)
print("{} / {} = {}".format(a, b, resultdiv))
