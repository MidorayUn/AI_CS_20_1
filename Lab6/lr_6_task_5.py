# -*- coding: utf-8 -*-
"""lr_6_task_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r6zyEAujao4dxZIoC3t44PoC63Y6vMev
"""

!pip install neurolab

import numpy as np
import neurolab as nl

target = [
    [0, 1, 0, 1, 0,
     1, 0, 1, 0, 1,
     1, 1, 1, 1, 1,
     1, 0, 0, 0, 1,
     0, 1, 0, 1, 0],

    [1, 1, 1, 1, 1,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 1,
     1, 1, 1, 1, 1],

    [0, 1, 1, 1, 0,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 1,
     0, 1, 1, 1, 0]
]

chars = ['І', 'О', 'Ю']
target = np.asfarray(target)
target[target == 0] = -1

# Create and train network
net = nl.net.newhop(target)
output = net.sim(target)
print("Test on train samples:")
for i in range(len(target)):
    print(chars[i], np.allclose(output[i], target[i], atol=1e-2))  # Змінено умову порівняння

print("\nTest on defaced І:")
test = np.asfarray([1, 1, 1, 1, 1,
                    1, 0, 0, 0, 1,
                    0, 1, 0, 1, 0,
                    0, 1, 0, 1, 0,
                    1, 1, 1, 1, 1])
test[test == 0] = -1
out = net.sim([test])
print(np.allclose(out[0], target[0], atol=1e-2), 'Sim. steps', len(net.layers[0].outs))  # Змінено умову порівняння

print("\nTest on defaced О:")
test_O = np.asfarray([1, 1, 1, 1, 1,
                      1, 0, 0, 0, 1,
                      1, 0, 0, 0, 1,
                      1, 0, 0, 0, 1,
                      1, 1, 1, 1, 1])
test_O[test_O == 0] = -1
out_O = net.sim([test_O])
print(np.allclose(out_O[0], target[1], atol=1e-2), 'Sim. steps', len(net.layers[0].outs))  # Змінено умову порівняння

print("\nTest on defaced Ю:")
test_Yu = np.asfarray([0, 1, 1, 1, 0,
                       1, 0, 0, 0, 1,
                       1, 0, 0, 0, 1,
                       1, 0, 0, 0, 1,
                       0, 1, 1, 1, 0])
test_Yu[test_Yu == 0] = -1
out_Yu = net.sim([test_Yu])
print(np.allclose(out_Yu[0], target[2], atol=1e-2), 'Sim. steps', len(net.layers[0].outs))  # Змінено умову порівняння

