import tensorflow as tf
import numpy as np

sess = tf.Session()

x_data=np.linspace(-1,1,300)[:, np.newaxis]
# print(x_data)
noise=np.random.normal(0, 0.05, x_data.shape)
# print(noise)
y_data=np.square(x_data) - 0.5 + noise
# print(y_data)

xs=tf.placeholder(tf.float32, [None, 1])
ys=tf.placeholder(tf.float32, [None, 1])

W1=tf.Variable(tf.random_normal([1, 10]))
b1=tf.Variable(tf.constant(0.1, shape=[1, 10]))
# print(sess.run(tf.constant(0.1, shape=[1, 10])))

Wx_plus_b1=tf.matmul(xs, W1) + b1
output1 = tf.nn.relu(Wx_plus_b1)

W2=tf.Variable(tf.random_normal([10, 1]))
b2=tf.Variable(tf.constant(0.1, shape=[1,1]))

Wx_plus_b2 = tf.matmul(output1, W2) + b2
output2 = Wx_plus_b2

loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-output2), reduction_indices=[1]))
train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init=tf.global_variables_initializer()
sess.run(init)

# print(x_data, y_data)

for i in range(1000):
    _, loss_value= sess.run([train_step, loss], feed_dict={xs:x_data, ys: y_data})
    if i%50 == 0:
        print(loss_value)
