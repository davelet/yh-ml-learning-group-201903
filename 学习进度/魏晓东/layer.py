import tensorflow as tf

sess = tf.Session()

x = tf.placeholder(tf.float32, shape=[None, 3])
linear_model = tf.layers.Dense(units=1)
y = linear_model(x)
print(y)

init = tf.global_variables_initializer()
sess.run(init)
print(init)
print(sess.run(y, {x: [[1,2,3],[4,5,6]]}))