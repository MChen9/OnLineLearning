from tensorpack.dataflow import *

class EchoServer:

    def __init__(self):
        ds0 = FakeData([[2,3]])
        send_dataflow_zmq(ds0, 'tcp://10.0.0.120:8877')