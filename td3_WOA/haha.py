import numpy as np
import time
import copy
import tensorflow as tf
import random
import math # cos() for Rastrigin
import sys # max float

log_dir = 'logs/'
train_summary_writer = tf.summary.create_file_writer(log_dir)

batch_size = 512
random_action_prob = 0.1

for i in range(200000):
    n_training=i
    with train_summary_writer.as_default():
        tf.summary.scalar('batch size', batch_size, step=n_training)
        tf.summary.scalar('rand act prob', random_action_prob, step=n_training)