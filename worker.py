import time
import zmq
import random
import math

# The worker component listens (PULL) the numbers
# from the generator in a round robin fashion and
# calculate a square root of the numbers.
# Finally, sends the result to the dashboard.

def worker():
    worker_id = [1, 2, 3]
    context = zmq.Context()
    # recieve work message
    worker_receiver = context.socket(zmq.PULL)
    worker_receiver.connect("tcp://127.0.0.1:1234")
    # send work result
    worker_sender = context.socket(zmq.PUSH)
    worker_sender.connect("tcp://127.0.0.1:1235")

    while True:
        work = worker_receiver.recv_json()
        data = work['num']
        sqrt = math.sqrt(int(data))
        # do work
        curWorker = worker_id[0]
        print("I am worker " + str(curWorker) + ". I received number " + str(data))
        worker_id.remove(curWorker)
        result = { 'worker' : curWorker, 'num' : data, 'sqrt': sqrt}
        worker_id.append(curWorker)
        worker_sender.send_json(result)
worker()
