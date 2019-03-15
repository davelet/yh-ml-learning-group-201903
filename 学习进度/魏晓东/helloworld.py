import tensorflow as tf

sess = tf.Session()

hello = tf.constant('hello world')
print(sess.run(hello))