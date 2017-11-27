import tensorflow as tf

W = tf.Variable([1],dtype=tf.float32);
b = tf.Variable([0],dtype=tf.float32);

x = tf.placeholder(tf.float32);
y = tf.placeholder(tf.float32);

linear_model = W*x + b;

loss = tf.reduce_sum(tf.square(linear_model-y));
optimizer = tf.train.GradientDescentOptimizer(0.01);
train = optimizer.minimize(loss);

x_train = [1,2,10,20,30,40,50];
y_train = [5,10,50,100,150,200,250];

init = tf.global_variables_initializer();

with tf.Session() as session:
    session.run(init);
    for i in range(1000):
        output = session.run(train, {x: x_train, y: y_train});
        print(output);
    curr_W, curr_b, curr_loss = session.run([W, b, loss], {x: x_train, y: y_train});
    print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss));
