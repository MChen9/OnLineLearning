from tensorpack.dataflow import *

class EchoServer:

    def __init__(self):
        while (True):
            ds0 = FakeData([[2,3]])
            send_dataflow_zmq(ds0, 'tcp://10.0.0.201:8877')











if __name__ == '__main__':
    echoServer = EchoServer()
