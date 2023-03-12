import numpy as np

f = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
label = np.array([0, 0, 0, 1])

# Take initial weight values as user input
w = input("Enter initial weight values separated by space: ").split()
w = [float(val) for val in w]

theta = float(input("Enter the value of Theta : "))
learning = float(input("Enter the value of learning rate : "))
n = -1
epoch = 5

for j in range(epoch):
    for i in range(f.shape[0]):
        actual = label[i]
        instance = f[i]

        x1 = instance[0]
        x2 = instance[1]

        net = w[0] * x1 + w[1] * x2 - theta

        if net > 0:
            y = 1
        else:
            y = 0

        delta = actual - y

        if delta != 0:
            w[0] = w[0] + learning * delta * x1
            w[1] = w[1] + learning * delta * x2
            theta = n * learning * delta + theta

        # Print updated weight values and equation after each iteration
        print("Iteration:", j+1, "Instance:", i+1)
        print("Updated weight values:", w)
        print("Updated equation: {} * x1 + {} * x2 - {} = 0".format(w[0], w[1], theta))
        print("Y=", y, "T-Y=", delta)
    print("******************")

