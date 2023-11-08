
import numpy as np
import matplotlib.pyplot as plt

# ----------- sigmoid activation function ----------- #
# Y = []
# def sigmoid(x):
#     for i in x:
#         Y.append(1 / (1 + math.exp(-i)))
#
#
# x = np.arange(-10, 10, 0.1)
# sigmoid(x)
# # print(Y)
#
# # plt.style.use('fivethirtyeight')
# plt.title('Sigmoid')
# plt.xlabel('x label')
# plt.ylabel('Y label')
# plt.plot(x, Y, '-r')
# plt.show()




# ---------- tanh activation function ----------- #
# Y = []
# def tanh(x):
#     for i in x:
#         Y.append((math.exp(i) - math.exp(-i)) / (math.exp(i) + math.exp(-i)))
#
#
# x = np.arange(-5, 5, 0.1)
# tanh(x)
#
# plt.title('tanh')
# plt.xlabel('x label')
# plt.ylabel('Y label')
# plt.plot(x, Y, '-m')
# plt.show()




# --------- relu activation function --------- #
# Y = []
# def relu(x):
#     for i in x:
#         Y.append(max(0, i))
#
# x = np.arange(-10, 10, 0.1)
# relu(x)
#
# plt.title('relu')
# plt.xlabel('x label')
# plt.ylabel('Y label')
# plt.plot(x, Y, '-b')
# plt.show()




# --------- leaky_relu activation function --------- #
Y = []
def leaky_relu(x):
    for i in x:
        Y.append(max(0.1*i, i))

x = np.arange(-100, 100, 0.1)
leaky_relu(x)

plt.title('leaky_rely')
plt.xlabel('x label')
plt.ylabel('Y label')
plt.plot(x, Y, '-g')
plt.show()