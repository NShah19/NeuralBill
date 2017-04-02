import numpy as np
import random
import tensorflow as tf

#take in array of sentiment analysis per twitter stream for 10 bills, train on 5, test on 3,
#return array of prediction with confidences
def create_feature_sets_and_labels(arr):
    # create train and test lists
    train_x = list(arr[:,0][:5])
    train_y = list(arr[:,1][:5])
    test_x = list(arr[:,0][5:8])
    test_y = list(arr[:,1][5:8])
    other_x = list(arr[:,0][8:])
    other_y = list(arr[:,1][8:])
    return train_x, train_y, test_x, test_y, other_x, other_y

train_x, train_y, test_x, test_y, other_x, other_y = create_feature_sets_and_labels()
