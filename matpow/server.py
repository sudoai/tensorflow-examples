import tensorflow as tf


CLUSTER = {
    'worker': ['localhost:2222', 'localhost:2223']
}

tf.app.flags.DEFINE_integer('task_index', 0, 'partition')


def cluster():
    return tf.train.ClusterSpec(CLUSTER)


def run(task_index):
    tf.train.Server(cluster(), job_name='worker', task_index=task_index).join()


if __name__ == '__main__':
    flags = tf.app.flags.FLAGS
    run(flags.task_index)

