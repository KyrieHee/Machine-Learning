#!/usr/bin/python
# -*- coding:utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

learning_rate = 0.01
x = 2
for i in range(1000):
    x -= learning_rate * (x**x * (np.log(x) + 1))
print(x, 1/x)

print("\n****************************************")

x = np.linspace(0.0001, 1, 50)
print(x)
y = x ** x
plt.plot(x, y, 'r-', lw=2)
plt.show()



print("\n****************************************")


if __name__ == "__main__":
     learning_rate = 0.01
     for a in range(1,100):
         cur = 0
         for i in range(1000):
             cur -= learning_rate*(cur**2 - a)
         print(' %d的平方根(近似)为：%.8f，真实值是：%.8f' % (a, cur, math.sqrt(a)))
