import time
import zmq
import pprint

def dashboard():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:1235")
    while True:
        result = results_receiver.recv_json()
        print(result)

dashboard()
