import numpy as np
import random
import tensorflow as tf

#take in array of sentiment analysis per twitter stream for 10 bills, train on 5, test on 3,
#return array of prediction with confidences
arr = []
testList = list(range(0, 136))
testOut = [1]
for i in range(10):
    arr.append([testList, testOut])
arr = np.array(arr)

def create_feature_sets_and_labels(arr):
    # create train and test lists
    train_x = list(arr[:,0][:5])
    train_y = list(arr[:,1][:5])
    test_x = list(arr[:,0][5:8])
    test_y = list(arr[:,1][5:8])
    other_x = list(arr[:,0][8:])
    other_y = list(arr[:,1][8:])
    return train_x, train_y, test_x, test_y, other_x, other_y

train_x, train_y, test_x, test_y, other_x, other_y = create_feature_sets_and_labels(arr)

# hidden layers and their nodes
n_nodes_hl1 = 20
n_nodes_hl2 = 20

# classes in our output
n_classes = 1
# iterations and batch-size to build out model
hm_epochs = 500
batch_size = 136

x = tf.placeholder('float')
y = tf.placeholder('float')


hidden_1_layer = {'f_fum':n_nodes_hl1,
                  'weight':tf.Variable(tf.random_normal([len(train_x[0]), n_nodes_hl1])),
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl1]))}

hidden_2_layer = {'f_fum':n_nodes_hl2,
                  'weight':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl2]))}

output_layer = {'f_fum':None,
                'weight':tf.Variable(tf.random_normal([n_nodes_hl2, n_classes])),
                'bias':tf.Variable(tf.random_normal([n_classes])),}



def neural_network_model(data):

    # hidden layer 1: (data * W) + b
    l1 = tf.add(tf.matmul(data,hidden_1_layer['weight']), hidden_1_layer['bias'])
    l1 = tf.sigmoid(l1)

    # hidden layer 2: (hidden_layer_1 * W) + b
    l2 = tf.add(tf.matmul(l1,hidden_2_layer['weight']), hidden_2_layer['bias'])
    l2 = tf.sigmoid(l2)

    # output: (hidden_layer_2 * W) + b
    output = tf.matmul(l2,output_layer['weight']) + output_layer['bias']

    return output

def train_neural_network(x):
    # use the model definition
    prediction = neural_network_model(x)

    # formula for cost (error)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits( logits= prediction, labels = y) )
    # optimize for cost using GradientDescent
    optimizer = tf.train.GradientDescentOptimizer(1).minimize(cost)

    # Tensorflow session
    with tf.Session() as sess:
        summary_writer = tf.summary.FileWriter('log_ANN_graph', sess.graph)
        # initialize our variables
        sess.run(tf.global_variables_initializer())

        # loop through specified number of iterations
        for epoch in range(hm_epochs):
            epoch_loss = 0
            i=0
            # handle batch sized chunks of training data
            while i < len(train_x):
                start = i
                end = i+batch_size
                batch_x = np.array(train_x[start:end])
                batch_y = np.array(train_y[start:end])

                _, c = sess.run([optimizer, cost], feed_dict={x: batch_x, y: batch_y})
                epoch_loss += c
                i+=batch_size
                last_cost = c

            # print cost updates along the way
            if (epoch% (hm_epochs/5)) == 0:
                print('Epoch', epoch, 'completed out of',hm_epochs,'cost:', last_cost)

        # print accuracy of our model
        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print('Accuracy:',accuracy.eval({x:test_x, y:test_y}))

        # print predictions using our model
        for i,t in enumerate(test_x):
            print ('prediction for:', test_x[i])
            output = prediction.eval(feed_dict = {x: [test_x[i]]})
            # normalize the prediction values
            print(tf.sigmoid(output[0][0]).eval(), tf.sigmoid(output[0][1]).eval())

train_neural_network(x)
