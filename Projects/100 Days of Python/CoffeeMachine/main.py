from menu import costs, resources
from take_request import take_request


def init():
    active = True
    while active:
        status = take_request(costs, resources)
        if status == "exit":
            active = False



init()

# TODO: 1. create init function to take request
# TODO: 2. check request against resources and cost
