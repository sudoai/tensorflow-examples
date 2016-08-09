import datetime

import numpy as np
import tensorflow as tf

n = 100000
m = 10

def mat_pow(matrix, power):
    _, r = tf.while_loop(
        lambda i, _: i > 0,
        lambda i, c: [i-1, tf.matmul(c, matrix, transpose_a=True)],
        [power, matrix],
        parallel_iterations=1,
        back_prop=False,
        swap_memory=False
    )
    return r


def random_matrix():
    x = np.random.rand(m, m)
    x_sum = np.sum(x, axis=0)
    return (x / x_sum).astype('float32')


def run_multi_node(data_a, data_b):
    t1 = datetime.datetime.now()
    with tf.device('/job:worker/task:0'):
        a = tf.constant(data_a, tf.float32)
        c1 = mat_pow(a, tf.constant(n))
        c1 = tf.Print(c1, [c1], message='Completed mat_pow ')
    with tf.device('/job:worker/task:1'):
        b = tf.constant(data_b, tf.float32)
        c2 = mat_pow(b, tf.constant(n))
        c2 = tf.Print(c2, [c2], message='Completed mat_pow ')

    with tf.Session('grpc://localhost:2222'):
        add = c1 + c2
        add.eval()
    t2 = datetime.datetime.now()
    print('Multi node computation time: %s' % str(t2-t1))


def run_single_node(data_a, data_b):
    t1 = datetime.datetime.now()

    a = tf.constant(data_a, tf.float32)
    c1 = mat_pow(a, tf.constant(n))
    c1 = tf.Print(c1, [c1], message='Completed mat_pow ')

    b = tf.constant(data_b, tf.float32)
    c2 = mat_pow(b, tf.constant(n))
    c2 = tf.Print(c2, [c2], message='Completed mat_pow ')

    add = c1 + c2
    with tf.Session():
        add.eval()
    t2 = datetime.datetime.now()
    print('Single node computation time: %s' % str(t2-t1))


def __main__():
    data_a = random_matrix()
    data_b = random_matrix()
    run_single_node(data_a, data_b)
    run_multi_node(data_a, data_b)


if __name__ == '__main__':
    __main__()
