import tensorflow as tf

sess = tf.Session()
my_data = [
	[0,1,],
	[2,3,],
	[4,5,],
	[6,7,],
]
slices = tf.data.DataSet.from_tensor_slice(my_data)
next_item=slices.make_one_shot_iterator().get_next()

while True:
	try:
		print(sess.run(next_item))
	except tf.errors.OutOfRangeError:
		break

