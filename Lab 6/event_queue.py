from priority_queue import *

# A EventQueue is
# A None or
# A Priority Queue
# Takes a Priority Queue and tracks a virtual time
class EventQueue():
    def __init__(self, pqueue = None, time = 0):
        self.pqueue = Pqueue() if pqueue == None else pqueue
        self.time = time

    def __repr__(self):
        return ("EventQueue({!r}, {!r})".format(self.pqueue, self.time))

    def __eq__(self, other):
        if isinstance(self, other):
            return self.pqueue == other.pqueue and self.time == other.time
        else:
            return False


# A add_event is
# A eventqueue
# EventQueue function number -> EventQueue
# Takes a eventqueue, event, and time delay and returns a new EventQueue with the even stored inside
def add_event(queue, event, delay):
    pass

# A run_event is
# A function
# Takes in an Eventqueue and runes queued events based on their delays
def run_event(queue):
    pass