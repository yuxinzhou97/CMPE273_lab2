import time
import zmq
import random

# The generator component generates a list of numbers
# from 0 to 10,000 and sends (PUSH) those numbers to Worker.

def generator():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:1234")
    # generate 50 numbers from from 0 to 10,000
    numbers = []
    for index in range(50):
        numbers.append(random.randrange(10000))
        num = numbers[index]
        work_message = { 'num' : num }
        zmq_socket.send_json(work_message)
        print("generator sends number: " + str(num))
generator()
