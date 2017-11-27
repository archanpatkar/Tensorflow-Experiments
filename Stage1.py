import tensorflow as tf

node1 = tf.constant(1);
print(node1);
node2 = tf.constant(3);
print(node2);
node3 = node1 + node2;
print(node3);

with tf.Session() as session:
    output = session.run(node3);
    print(output);
