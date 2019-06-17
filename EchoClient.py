from tensorpack.dataflow import *


class EchoClient:

    def __init__(self):
        df = RemoteDataZMQ('tcp://10.0.0.120:28877')

        pass


if __name__ == '__main__':
    echoClient = EchoClient()
