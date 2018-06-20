from tensorflow.examples.tutorials.mnist import input_data

# 载入mnisst数据集,如果指定目录下没有,就会下载
mnist = input_data.read_data_sets("../../data/mnist/")

# 打印训练数据大小
# print(mnist.train.num_examples) # 55000

#
# print(mnist.validation.num_examples)    # 5000

# print(mnist.test.num_examples) # 10000

# print(mnist.train.images[0])
'''
[0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.3803922  0.37647063 0.3019608
 0.46274513 0.2392157  0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.3529412
 0.5411765  0.9215687  0.9215687  0.9215687  0.9215687  0.9215687
 0.9215687  0.9843138  0.9843138  0.9725491  0.9960785  0.9607844
 0.9215687  0.74509805 0.08235294 0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.54901963 0.9843138  0.9960785  0.9960785
 0.9960785  0.9960785  0.9960785  0.9960785  0.9960785  0.9960785
 0.9960785  0.9960785  0.9960785  0.9960785  0.9960785  0.9960785
 0.7411765  0.09019608 0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.8862746  0.9960785  0.81568635 0.7803922  0.7803922  0.7803922
 0.7803922  0.54509807 0.2392157  0.2392157  0.2392157  0.2392157
 0.2392157  0.5019608  0.8705883  0.9960785  0.9960785  0.7411765
 0.08235294 0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.14901961 0.32156864
 0.0509804  0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.13333334 0.8352942  0.9960785  0.9960785  0.45098042 0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.32941177
 0.9960785  0.9960785  0.9176471  0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.32941177 0.9960785  0.9960785
 0.9176471  0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.4156863  0.6156863  0.9960785  0.9960785  0.95294124 0.20000002
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.09803922
 0.45882356 0.8941177  0.8941177  0.8941177  0.9921569  0.9960785
 0.9960785  0.9960785  0.9960785  0.94117653 0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.26666668 0.4666667  0.86274517 0.9960785  0.9960785
 0.9960785  0.9960785  0.9960785  0.9960785  0.9960785  0.9960785
 0.9960785  0.5568628  0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.14509805 0.73333335 0.9921569
 0.9960785  0.9960785  0.9960785  0.8745099  0.8078432  0.8078432
 0.29411766 0.26666668 0.8431373  0.9960785  0.9960785  0.45882356
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.4431373  0.8588236  0.9960785  0.9490197  0.89019614 0.45098042
 0.34901962 0.12156864 0.         0.         0.         0.
 0.7843138  0.9960785  0.9450981  0.16078432 0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.6627451  0.9960785
 0.6901961  0.24313727 0.         0.         0.         0.
 0.         0.         0.         0.18823531 0.9058824  0.9960785
 0.9176471  0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.07058824 0.48627454 0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.32941177 0.9960785  0.9960785  0.6509804  0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.54509807
 0.9960785  0.9333334  0.22352943 0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.8235295  0.9803922  0.9960785  0.65882355
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.9490197  0.9960785  0.93725497 0.22352943 0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.34901962 0.9843138  0.9450981
 0.3372549  0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.01960784 0.8078432  0.96470594 0.6156863  0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.01568628 0.45882356
 0.27058825 0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.        ]
'''

# print(mnist.train.labels[0])    # 7

batch_size = 100
xs, ys = mnist.train.next_batch(batch_size)
print(xs.shape)
print(ys.shape)
'''
(100, 784)
(100,)
'''