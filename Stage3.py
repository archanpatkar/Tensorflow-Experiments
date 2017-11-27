import tensorflow as tf

node1 = tf.constant(1);
print(node1);
node2 = tf.constant(3);
print(node2);
node3 = node1 + node2;
print(node3);

node4 = tf.placeholder(tf.int32);
print(node4);
node5 = tf.placeholder(tf.int32);
print(node5);

node6 = node4 + node5;
print(node6);

node7 = node3 + node6;
print(node7);

with tf.Session() as session:
    output = session.run([node3,node6,node7],{node4:[10,20,30,40,50],node5:[1,2,3,4,5]});
    print(output);
